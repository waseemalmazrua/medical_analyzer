from pydantic import BaseModel
from app.schemas.agent_output import ClinicalReport
from app.schemas.NER import entity
class AudioAnalyzerResponse(BaseModel):
    filename : str | None = None
    transcript : str
    entities : list[entity]
    report : ClinicalReport