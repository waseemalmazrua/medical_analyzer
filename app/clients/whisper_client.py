# app/clients/whisper_client.py
import os

import logfire
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class WhisperClient:
    def __init__(self) -> None:
        api_key = os.getenv("GROQ_API_KEY")
        if api_key is None:
            raise ValueError("groq key not found")

        self.client = Groq(api_key=api_key)

    def close(self):
        self.client.close()

    async def transcribe(
        self,
        filename: str,
        audio_bytes: bytes,
        content_type: str,
    ) -> dict:

        with logfire.span("Call Whisper Service", text_legth=len(audio_bytes)):
            transcription = self.client.audio.transcriptions.create(
                file=(filename, audio_bytes),
                model="whisper-large-v3-turbo",
                temperature=0,
                language="en",
            )

            # print("the Model Dumb is : ",transcription.model_dump())

            transcript = transcription.text

            logfire.info(
                "Transcription Completed",
                transcript_legth=len(transcript),
            )

            return {"transcript": transcript}


# BentoML Client

# class WhisperClient:
#     def __init__(self, base_url: str = "http://localhost:3002"):
#         self.base_url = base_url

#     async def transcribe(
#         self,
#         filename: str,
#         audio_bytes: bytes,
#         content_type: str,
#     ) -> dict:

#         # with logfire.span("Call Whisper Service"):

#             async with httpx.AsyncClient(timeout=300) as client:

#                 response = await client.post(
#                     f"{self.base_url}/transcribe",
#                     files={
#                         "file": (
#                             filename,
#                             audio_bytes,
#                             content_type,
#                         )
#                     },
#                 )

#                 response.raise_for_status()

#                 return response.json()
