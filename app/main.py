from fastapi import FastAPI
from app.api.medical import router as medical_router
from app.core.logging import setup_observability
from app.lifespans.lifespan_services import lifespan

app = FastAPI(lifespan=lifespan,title="Medical Analyzer API")

# Setup Logfire tracing
setup_observability(app)

app.include_router(medical_router)


@app.get("/")
def health_check():
    return {"message": "Welcome to Medical Analyzer AI"}