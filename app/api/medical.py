# app/api/routes.py

from fastapi import APIRouter, UploadFile, File , HTTPException , Request

from app.clients.whisper_client import WhisperClient
from app.clients.ner_client import NERClient
from app.agents.analyzer_agent import generate_clinical_report
from app.schemas.audio_analyzer_response import AudioAnalyzerResponse

router =  APIRouter(
    prefix="/medical",
    tags=["Medical Analysis"]
)

# whisper_client = WhisperClient()
# ner_client = NERClient()


@router.post("/analyze-audio")
async def analyze_audio(
    request: Request,
    file: UploadFile = File(...),
) -> AudioAnalyzerResponse:
    
    if not file.content_type or not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid audio file")
    
    try:

        services = request.app.state.services
    # اقرأ ملف الصوت
        audio_bytes = await file.read()

        # 1) Whisper ASR
        whisper_result = await services.whisper.transcribe(
            filename=file.filename,
            audio_bytes=audio_bytes,
            content_type=file.content_type,
        )

        transcript = whisper_result["transcript"]

        # 2) Medical NER
        ner_result = await services.ner.extract_entities(
            transcript
        )

        entities = ner_result.entities

        # 3) AI Agent
        report = await generate_clinical_report(
            transcript=transcript,
            entities=entities,
        )

        # 4) Final Response
        return AudioAnalyzerResponse(
            filename=file.filename,
            transcript=transcript,
            entities=entities,
            report=report
        )


    except HTTPException:
        raise


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
