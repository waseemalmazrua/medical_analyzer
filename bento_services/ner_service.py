# bento_services/ner_service.py

import bentoml
from gliner import GLiNER
import logfire
logfire.configure(service_name="NERService",distubution_tracing=True)
@bentoml.service(traffic={"timeout": 120})
class NERService:
    def __init__(self):
        self.model = GLiNER.from_pretrained(
            "Ihor/gliner-biomed-large-v1.0"
        )

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
    def extract_entities(self, text: str) -> dict:

        with logfire.span("gliner predict",text_legth=len(text)):

            entities = self.model.predict_entities(
                text,
                self.labels,
                threshold=0.5,
            )

            return {
                "entities": entities
            }