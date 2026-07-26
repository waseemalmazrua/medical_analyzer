# app/clients/ner_client.py

import httpx
import logfire
from app.schemas.NER import NEROutput , NerRequest
import os
from dotenv import load_dotenv
load_dotenv()

runpod = os.getenv("RUNPOD_API_KEY")

if not runpod:
    raise RuntimeError("RUNPOD_API_KEY is not loaded")

class NERClient:
    def __init__(self, base_url: str = "https://qp4puae2rabqjl.api.runpod.ai" ):
        self.base_url = "http://localhost:3001"
        self.client = httpx.AsyncClient(timeout=300)



        
    async def aclose(self):
        await self.client.aclose()
    
    
    

    async def extract_entities(self, NerRequest: NerRequest) -> NEROutput:

        with logfire.span("Call NER Service",text_legth=len(NerRequest.text)):

                response = await self.client.post(
                    f"{self.base_url}/extract_entities",
                    json={
                        "text": NerRequest.text
                    },
                    headers={
                        "Authorization": f"Bearer {runpod}"
                    },
                    
                )

                response.raise_for_status()
                data = response.json()

                return NEROutput.model_validate(data)
