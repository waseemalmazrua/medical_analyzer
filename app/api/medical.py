# app/api/routes.py

from typing import Annotated

import httpx
from fastapi import APIRouter, File, HTTPException, Request, UploadFile

from app.agents.analyzer_agent import generate_clinical_report
from app.schemas.audio_analyzer_response import AudioAnalyzerResponse
from bento_services.ner_schema import NerRequest

router = APIRouter(tags=["Medical Analysis"])

# whisper_client = WhisperClient()
# ner_client = NERClient()


@router.post("/analyze-audio")
async def analyze_audio(
    request: Request,
    file: Annotated[UploadFile, File()],
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
        ner_result = await services.ner.extract_entities(NerRequest(text=transcript))

        entities = ner_result.entities

        # 3) AI Agent
        report = await generate_clinical_report(
            transcript=transcript,
            entities=entities,
        )

        # 4) Final Response
        return AudioAnalyzerResponse(
            report=report,
        )

    except HTTPException:
        raise

    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Upstream service request failed.",
        ) from exc
