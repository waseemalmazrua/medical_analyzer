from fastapi import FastAPI
from redis_fastapi import FastAPIRedis

from app.api.medical import router as medical_router
from app.core.logging import setup_observability
from app.lifespans.lifespan_services import lifespan

app = FastAPI(lifespan=lifespan, title="Medical Analyzer API")
FastAPIRedis(app).lifespan().rate_limiting().otel()

# Setup Logfire tracing
setup_observability(app)

app.include_router(medical_router)


@app.get("/")
def health_check():
    return {"message": "Welcome to Medical Analyzer AI"}
