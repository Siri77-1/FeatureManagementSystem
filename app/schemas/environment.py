from pydantic import BaseModel
from typing import Optional


class EnvironmentCreate(BaseModel):
    name: str
    description: str


class EnvironmentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class EnvironmentResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True