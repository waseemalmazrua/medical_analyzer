
import logfire
from pydantic_ai import Agent

from app.core.config import settings
from app.schemas.agent_output import ClinicalReport

api_key = settings.openai_api_key.get_secret_value()
if api_key is None:
    raise ValueError("OPENAI API key is not available")


clinical_agent = Agent(
    "openai:gpt-5.2",
    output_type=ClinicalReport,
    instructions="""
You are a clinical documentation assistant.

Use the transcript and extracted medical entities to generate a structured clinical report.

Rules:
- Do not invent information not present in the transcript.
- If information is missing, say "Not documented".
- Keep the output concise.
- clinical_summary: maximum 120 words.
- key_findings: maximum 5 items.
- possible_risks: maximum 3 items.
- Keep each SOAP section concise.
- recommendations: maximum 3 items.
- Each recommendation rationale must be one short sentence.
- Do not repeat the same information across sections.
- Recommendations must be cautious and require clinician review.
- Always include this disclaimer:
  "AI-generated output. Must be reviewed by a licensed clinician."
""",
)


async def generate_clinical_report(
    transcript: str,
    entities: list[dict],
) -> ClinicalReport:
    prompt = f"""
Transcript:
{transcript}

Extracted entities:
{entities}

Generate a structured clinical report.
"""

    with logfire.span(
        "clinical_agent run",
        transcript_length=len(transcript),
        entities_count=len(entities),
        prompt_characters=len(prompt),
    ):
        result = await clinical_agent.run(prompt)

        usage = result.usage().input_tokens

        logfire.info(
            "LLM completed",
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            total_tokens=usage.total_tokens,
        )

    return result.output