# app/clients/ner_client.py


import httpx
import logfire

from bento_services.ner_config import ner_settings
from bento_services.ner_schema import NEROutput, NerRequest

runpod = ner_settings.runpod_api_key.get_secret_value()

if not runpod:
    raise RuntimeError("RUNPOD_API_KEY is not loaded")




class NERClient:
    def __init__(self, base_url: str = "https://dwzrda6b7rcpum.api.runpod.ai"):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=300)

    async def aclose(self):
        await self.client.aclose()

    async def extract_entities(self, request: NerRequest) -> NEROutput:
        with logfire.span(
            "Call NER Service",
            text_length=len(request.text),
        ):
            try:
                response = await self.client.post(
                    f"{self.base_url}/extract_entities",
                    json={"text": request.text},
                    headers={
                        "Authorization": f"Bearer {runpod}",
                    },
                )

                response.raise_for_status()

                return NEROutput.model_validate(response.json())

            except httpx.HTTPStatusError as e:
                logfire.error(
                    "NER service returned HTTP error",
                    status_code=e.response.status_code,
                    response=e.response.text,
                    url=str(e.request.url),
                )
                raise

            except httpx.RequestError as e:
                logfire.error(
                    "NER service request failed",
                    error=str(e),
                    url=str(e.request.url),
                )
                raise

            except Exception:
                logfire.exception("Unexpected NER client error")
                raise