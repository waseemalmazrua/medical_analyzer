import logfire
from fastapi import FastAPI


def setup_logging(app: FastAPI) -> None:
    print("LOGFIRE ENABLED...")

    logfire.configure()

    # FastAPI tracing
    logfire.instrument_fastapi(app)

    # HTTP requests tracing
    logfire.instrument_httpx()

    # Pydantic AI tracing
    logfire.instrument_pydantic_ai()