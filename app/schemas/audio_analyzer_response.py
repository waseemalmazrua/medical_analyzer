from pydantic import BaseModel

from app.schemas.agent_output import ClinicalReport
from app.schemas.ner import Entity


class AudioAnalyzerResponse(BaseModel):
    filename: str | None = None
    transcript: str
    entities: list[Entity]
    report: ClinicalReport
