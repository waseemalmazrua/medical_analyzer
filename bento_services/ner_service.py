# bento_services/ner_service.py

import bentoml
from gliner import GLiNER
import torch
import logfire
import os
from dotenv import load_dotenv
from app.schemas.NER import NEROutput


load_dotenv()
token = os.getenv("LOGFIRE_TOKEN")
if token is None:
    raise ValueError(" token logfire not available")

    
logfire.configure(token=token,service_name="NERService",distributed_tracing=True)
image = (
    bentoml.images.Image(
        base_image="python:3.11-slim"
    )
    .python_packages(
        "bentoml==1.4.38",
        "gliner==0.2.24",
        "torch==2.11.0",
        "logfire==4.32.1",
        "python-dotenv>=1.2.2",
        
    )
)
@bentoml.service(image=image,resources={"gpu": 1},traffic={"timeout": 120})
class NERService:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = GLiNER.from_pretrained(
            "Ihor/gliner-biomed-large-v1.0"
        )
        self.model.to(device)
        print(f"GLiNER loaded on {device}")

        self.labels = [
            "disease",
            "medication",
            "symptom",
            "lab test",
            "lab test value",
            "dosage",
            "drug frequency",
            "demographic information",
        ]

    @bentoml.api
    def extract_entities(self, text: str) -> NEROutput:

        with logfire.span("Gliner predict",text_legth=len(text)):

            entities = self.model.predict_entities(
                text,
                self.labels,
                threshold=0.5,
            )
            # print(list(entities[0].keys()))

            return NEROutput(entities=entities)