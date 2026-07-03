from fastapi import FastAPI
from app.api.environment import router as environment_router

app = FastAPI(title="Application Feature Management API")

app.include_router(environment_router)


@app.get("/")
def home():
    return {"message": "Application Feature Management API"}