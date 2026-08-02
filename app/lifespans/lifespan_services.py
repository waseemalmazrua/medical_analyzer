from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.engine import engine
from app.lifespans.services import Services


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:

    app.state.services = Services()

    try:
        yield
    finally:
        app.state.services.whisper.close()
        await app.state.services.ner.aclose()
        await engine.dispose()
