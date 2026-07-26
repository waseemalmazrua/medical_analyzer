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
    chief_complaint: str | None
    clinical_summary: str
    key_findings: list[str]
    possible_risks: list[str]
    soap_note: SOAPNote
    recommendations: list[Recommendation]
    disclaimer: str
