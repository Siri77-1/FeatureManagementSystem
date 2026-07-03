from fastapi import FastAPI

from app.api.environment import router as environment_router
from app.api.feature_flag import router as feature_flag_router
from app.api.auth import router as auth_router
app = FastAPI(
    title="Application Feature Management API"
)

app.include_router(
    environment_router,
    prefix="/environments",
    tags=["Environments"]
)

app.include_router(
    feature_flag_router,
    prefix="/flags",
    tags=["Feature Flags"]
)
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]     
)
@app.get("/")
def home():
    return {"message": "Application Feature Management API"}