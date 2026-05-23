from fastapi import FastAPI
from app.api import medical
from app.core.logging import setup_logging


app = FastAPI(title="Medical Analyzer API")

# Setup Logfire tracing
setup_logging(app)

app.include_router(medical)


@app.get("/")
def read_root():
    return {"message": "Welcome to Medical Analyzer AI"}