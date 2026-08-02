from pydantic import BaseModel

from app.schemas.agent_output import ClinicalReport
from bento_services.ner_schema import Entity


class AudioAnalyzerResponse(BaseModel):
    filename: str | None = None
    transcript: str
    entities: list[Entity]
    report: ClinicalReport
