from fastapi import FastAPI
from app.api.medical import router as medical_router
from app.core.logging import setup_observability

app = FastAPI(title="Medical Analyzer API")

# Setup Logfire tracing
setup_observability(app)

app.include_router(medical_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Medical Analyzer AI"}