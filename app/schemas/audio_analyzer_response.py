from pydantic import BaseModel

from app.schemas.agent_output import ClinicalReport


class AudioAnalyzerResponse(BaseModel):
    report: ClinicalReport
