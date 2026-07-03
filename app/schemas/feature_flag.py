from pydantic import BaseModel
from typing import Optional


class FeatureFlagCreate(BaseModel):
    key: str
    description: Optional[str] = None
    type: str
    default_value: str
    enabled: bool = True
    owner_team: Optional[str] = None


class FeatureFlagUpdate(BaseModel):
    key: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    default_value: Optional[str] = None
    enabled: Optional[bool] = None
    owner_team: Optional[str] = None


class FeatureFlagResponse(BaseModel):
    id: int
    key: str
    description: Optional[str]
    type: str
    default_value: str
    enabled: bool
    owner_team: Optional[str]

    class Config:
        from_attributes = True