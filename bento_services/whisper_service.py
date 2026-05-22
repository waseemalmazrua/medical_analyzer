import bentoml
from pathlib import Path
from faster_whisper import WhisperModel
from gliner import GLiNER


@bentoml.service(traffic={"timeout": 300})
class MedicalAnalyzerService:

    def __init__(self):

        self.asr = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8",
        )

        self.ner_model = GLiNER.from_pretrained(
            "Ihor/gliner-biomed-large-v1.0"
        )

        self.labels = [
            "disease",
            "medication",
            "symptom",
            "lab test",
            "lab test value",
            "dosage",
            "drug frequency",
            "demographic information",
        ]

    def _transcribe_audio(self, audio_path: Path) -> str:
        segments, info = self.asr.transcribe(
            str(audio_path),
            language="en",
            vad_filter=True,
        )

        transcript = " ".join(segment.text.strip() for segment in segments)
        return transcript

    def _extract_entities(self, text: str) -> list:
        return self.ner_model.predict_entities(
            text,
            self.labels,
            threshold=0.5,
        )

    @bentoml.api
    def analyze_audio(self, file: Path) -> dict:
        transcript = self._transcribe_audio(file)
        entities = self._extract_entities(transcript)

        return {
            "filename": file.name,
            "transcript": transcript,
            "entities": entities,
        }