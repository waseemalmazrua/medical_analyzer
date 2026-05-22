# bento_services/whisper_service.py

import bentoml
from pathlib import Path
from faster_whisper import WhisperModel


@bentoml.service(traffic={"timeout": 300})
class WhisperService:
    def __init__(self):
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8",
        )

    @bentoml.api
    def transcribe(self, file: Path) -> dict:
        segments, info = self.model.transcribe(
            str(file),
            language="en",
            vad_filter=True,
        )

        transcript = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return {
            "transcript": transcript,
            "language": info.language,
            "language_probability": info.language_probability,
        }