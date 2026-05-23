from typing import List, Optional
from pydantic import BaseModel, Field



class SOAPNote(BaseModel):
    subjective: str
    objective: str
    assessment: str
    plan: str


class Recommendation(BaseModel):
    title: str
    rationale: str
    urgency: str = Field(description="low, medium, or high")


class ClinicalReport(BaseModel):
    chief_complaint: Optional[str]
    clinical_summary: str
    key_findings: List[str]
    possible_risks: List[str]
    soap_note: SOAPNote
    recommendations: List[Recommendation]
    disclaimer: str
