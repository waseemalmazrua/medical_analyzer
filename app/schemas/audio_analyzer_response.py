from pydantic import BaseModel

from app.schemas.agent_output import ClinicalReport
from bento_services.ner_schema import Entity


class AudioAnalyzerResponse(BaseModel):
    report: ClinicalReport
