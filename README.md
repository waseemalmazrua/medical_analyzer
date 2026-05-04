# Claira - Clinical AI report Analyzer 

## Medical Analyzer

Smart medical report analysis — extracts diseases, medications, risks, and generates clinical recommendations.

---

## Overview

Upload a medical report (PDF or text) and the system will:

- Summarize the report in plain language
- Extract diseases, medications, and lab results
- Identify risk levels
- Provide actionable recommendations

---

## Tech Stack

| Tool | Role |
|------|------|
| `blaze999/Medical-NER` (HuggingFace) | Extract 41 medical entities |
| `Pydantic AI` | Agent orchestration + structured output |
| `FastAPI` | API logic and endpoints |
| `BentoML` | Model serving |
| `Logfire` | Monitoring and tracing |

---

## Architecture

```
PDF / Text Input
       ↓
   FastAPI  —  receives request
       ↓
HuggingFace NER  —  extracts entities (diseases, meds, labs)
       ↓
Pydantic AI Agent  —  structures output + generates recommendations
       ↓
BentoML  —  serves the NER model
       ↓
Logfire  —  monitors everything
```

---

## Installation

```bash
git clone https://github.com/waseemalmazrua/medical_analyzer
cd medical_analyzer

uv sync

cp .env.example .env
```

---

## Environment Variables

```env
ANTHROPIC_API_KEY=
LOGFIRE_TOKEN=
```

---

## Run

```bash
uv run uvicorn main:app --reload
```

- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/analyze` | Analyze medical report text |
| `POST` | `/analyze/pdf` | Upload and analyze PDF |
| `POST` | `/chat` | Chat with MedBot about the report |
| `GET` | `/health` | Health check |

---

## Example Output

```json
{
  "summary": "Patient has Type 2 Diabetes with hypertension and mild kidney impairment.",
  "diseases": ["Type 2 Diabetes", "Hypertension", "Mild CKD"],
  "medications": ["Metformin 1000mg", "Amlodipine 5mg", "Atorvastatin 20mg"],
  "risks": [
    { "label": "HbA1c", "value": 7.8, "level": "high" },
    { "label": "Creatinine", "value": 1.4, "level": "moderate" }
  ],
  "recommendations": [
    "Review Metformin dosage due to reduced kidney function",
    "Improve diet to control HbA1c",
    "Follow-up appointment in 4 weeks"
  ],
  "recommend_doctor": true,
  "confidence": 0.94
}
```

---

## Roadmap

- [x] Project setup
- [ ] HuggingFace NER integration
- [ ] Pydantic AI agent
- [ ] FastAPI endpoints
- [ ] BentoML model serving
- [ ] MedBot chatbot
- [ ] Frontend (React + Tailwind)
- [ ] Logfire monitoring

---

## Disclaimer

This tool is for informational purposes only and is not a substitute for professional medical advice.

---

## Author

Waseem Almazrua
