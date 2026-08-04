# CLAIRA — Clinical Language AI Reasoning Assistant

## Medical Voice Analyzer

AI-powered clinical voice analysis system that transforms doctor speech into structured medical intelligence.

---

## Overview

CLAIRA enables clinicians to record (maybe CLAIRA v2) or upload medical conversations and automatically generates structured clinical insights using AI.

The system can:

* Convert doctor speech into medical transcripts
* Extract diseases, symptoms, medications, dosages, labs, and demographics
* Generate structured clinical summaries
* Create SOAP notes and recommendations
* Highlight possible medical risks
* Provide AI-assisted clinical reasoning

---

## Tech Stack

| Tool                | Role                                       |
| ------------------- | ------------------------------------------ |
| `Faster-Whisper`    | Speech-to-text transcription               |
| `GLiNER Biomedical` | Medical entity extraction                  |
| `OPENAI GPT-5.2`    | Clinical reasoning + summarization         |
| `Pydantic AI`       | Structured AI orchestration and validation |
| `FastAPI`           | API gateway and orchestration              |
| `BentoML`           | Model serving and inference                |
| `httpx`             | Service-to-service communication           |
| `Logfire`           | Monitoring and tracing                     |

---

## Architecture

```text
Doctor Audio
      ↓
Whisper Service
(audio → transcript)
      ↓
Medical Correction Layer
(correct medical terminology)
      ↓
Medical NER Service
(extract symptoms, medications, diseases, labs)
      ↓
Pydantic AI Agent + GPT
(clinical reasoning + structured report)
      ↓
FastAPI Response
      ↓
Frontend Dashboard
```

---

## System Design

CLAIRA follows a microservice-based AI architecture.

### Services

| Service           | Responsibility                                  |
| ----------------- | ----------------------------------------------- |
| `Whisper Service` | Speech transcription                            |
| `NER Service`     | Medical entity extraction                       |
| `AI Agent Layer`  | Clinical reasoning and report generation        |
| `FastAPI Gateway` | Request orchestration                           |
| `Frontend`        | Recording, transcript, and report visualization |

---

## Features

* Medical voice recording
* Audio upload support
* AI-powered transcription
* Medical entity extraction
* Structured clinical summaries
* SOAP note generation
* Risk analysis
* Clinical recommendations
* Exportable reports
* Real-time monitoring

---

## Example Pipeline

```text
Doctor Voice
↓
Whisper converts speech into text
↓
Medical NER extracts:
- Diseases
- Symptoms
- Medications
- Dosages
- Lab results
↓
AI Agent generates:
- Clinical Summary
- SOAP Note
- Risk Analysis
- Recommendations
```


---

## API Endpoints

| Method | Endpoint                 | Description              |
| ------ | ------------------------ | ------------------------ |
| `POST` | `/medical/analyze-audio` | Analyze medical audio    |
| `POST` | `/medical/upload-audio`  | Upload and analyze audio |
| `GET`  | `/health`                | Health check             |

---

## Example Output

```json
{
  "transcript": "Patient reports chest pain and shortness of breath.",

  "entities": {
    "symptoms": [
      "chest pain",
      "shortness of breath"
    ],
    "conditions": [
      "hypertension"
    ],
    "medications": [
      "aspirin"
    ]
  },

  "report": {
    "clinical_summary": "Patient presents with cardiopulmonary symptoms.",

    "possible_risks": [
      "Acute coronary syndrome"
    ],

    "recommendations": [
      {
        "title": "ECG",
        "urgency": "high"
      }
    ]
  }
}
```

---

## Frontend Vision

The frontend is designed as a modern clinical dashboard.

Features include:

* Voice recording (possible CLAIRA:v2)
* Live recording indicators
* Transcript visualization
* Highlighted medical entities
* Clinical summary cards
* SOAP note viewer
* Export functionality
* Responsive healthcare-grade UI

---

## Roadmap

* [x] Faster-Whisper integration
* [x] Medical NER pipeline
* [x] Pydantic AI structured outputs
* [x] BentoML microservices
* [ ] Real-time streaming transcription
* [x] React frontend
* [x] Authentication system
* [x] PDF export
* [x] Docker deployment
* [x] Cloud GPU deployment
* [ ] Multi-language support

---

## Disclaimer

CLAIRA is intended for clinical assistance and research purposes only.

AI-generated outputs must always be reviewed by qualified healthcare professionals.

---

## Author

Waseem Almazrua
