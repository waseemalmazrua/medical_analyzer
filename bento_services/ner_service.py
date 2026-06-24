# bento_services/ner_service.py

import bentoml
from gliner import GLiNER
import torch
import logfire
from app.schemas.NER import NEROutput

logfire.configure(service_name="NERService",distributed_tracing=True)
@bentoml.service(resources={"gpu": 1},traffic={"timeout": 120})
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