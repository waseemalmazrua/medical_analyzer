# app/clients/ner_client.py

import httpx
import logfire
from app.schemas.NER import NEROutput

class NERClient:
    def __init__(self, base_url: str = "http://localhost:3001"):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=200)
    
    
    

    async def extract_entities(self, text: str) -> NEROutput:

        with logfire.span("Call NER Service",text_legth=len(text)):

                response = await self.client.post(
                    f"{self.base_url}/extract_entities",
                    json={
                        "text": text
                    },
                    
                )

                response.raise_for_status()
                data = response.json()

                return NEROutput.model_validate(data)