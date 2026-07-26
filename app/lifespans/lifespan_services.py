from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.lifespans.services import Services

@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.services = Services()

    try:
        yield
    finally:
             
             app.state.services.whisper.close()
             await app.state.services.ner.aclose()

    