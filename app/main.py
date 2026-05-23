from fastapi import FastAPI
from app.api import medical


app = FastAPI(title="Medical Analyzer API")


app.include_router(medical)

@app.get("/")
def read_root():
    return {"message": "Welcome to Medical Analyzer AI"}