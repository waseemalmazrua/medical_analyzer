from pydantic_ai import Agent
import logfire
from app.schemas.agent_output import ClinicalReport
import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv("OPENAI_API_KEY")

clinical_agent = Agent(
    "openai:gpt-5.2",
    output_type=ClinicalReport,
    system_prompt="""
You are a clinical documentation assistant.

Use the transcript and extracted medical entities to generate a structured clinical report.

Rules:
- Do not invent information not present in the transcript.
- If information is missing, say "Not documented".
- Recommendations must be cautious and require clinician review.
- Always include this disclaimer:
  "AI-generated output. Must be reviewed by a licensed clinician."
"""
)


async def generate_clinical_report(
    transcript: str,
    entities: list,
) -> ClinicalReport:


    prompt = f"""
Transcript:
{transcript}

Extracted entities:
{entities}

Generate a structured clinical report.
"""

    result = await clinical_agent.run(prompt)
    return result.output