# app/clients/whisper_client.py
import httpx
import logfire


class WhisperClient:
    def __init__(self, base_url: str = "http://localhost:3002"):
        self.base_url = base_url

    async def transcribe(
        self,
        filename: str,
        audio_bytes: bytes,
        content_type: str,
    ) -> dict:

        # with logfire.span("Call Whisper Service"):

            async with httpx.AsyncClient(timeout=300) as client:

                response = await client.post(
                    f"{self.base_url}/transcribe",
                    files={
                        "file": (
                            filename,
                            audio_bytes,
                            content_type,
                        )
                    },
                )

                response.raise_for_status()

                return response.json()