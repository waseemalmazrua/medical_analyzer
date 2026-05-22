import logfire

def setup_logging(app):

    logfire.configure()

    # FastAPI tracing
    logfire.instrument_fastapi(app)

    # HTTP requests tracing
    logfire.instrument_httpx()

    # Pydantic AI tracing
    logfire.instrument_pydantic_ai()