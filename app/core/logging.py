import logfire
from fastapi import FastAPI


def setup_logging(app: FastAPI) -> None:
    print("LOGFIRE ENABLED...")

    logfire.configure(service_name="CLAIRA",distributed_tracing=True)

    # FastAPI tracing
    logfire.instrument_fastapi(app)

    # HTTP requests tracing
    logfire.instrument_httpx()

    # Pydantic AI tracing
    logfire.instrument_pydantic_ai()