# app/clients/ner_client.py

import httpx


class NERClient:
    def __init__(self, base_url: str = "http://localhost:3001"):
        self.base_url = base_url

    async def extract_entities(self, text: str) -> dict:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{self.base_url}/extract_entities",
                json={
                    "text": text
                },
            )

            response.raise_for_status()
            return response.json()