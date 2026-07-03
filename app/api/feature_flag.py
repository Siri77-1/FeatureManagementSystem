from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.schemas.feature_flag import (
    FeatureFlagCreate,
    FeatureFlagUpdate,
    FeatureFlagResponse,
)
from app.services import feature_flag_service

router = APIRouter()


@router.post("/", response_model=FeatureFlagResponse)
def create(flag: FeatureFlagCreate, db: Session = Depends(get_db)):
    return feature_flag_service.create_flag(db, flag)


@router.get("/", response_model=list[FeatureFlagResponse])
def read_all(db: Session = Depends(get_db)):
    return feature_flag_service.get_flags(db)


@router.get("/{flag_id}", response_model=FeatureFlagResponse)
def read_one(flag_id: int, db: Session = Depends(get_db)):
    flag = feature_flag_service.get_flag(db, flag_id)
    if not flag:
        raise HTTPException(status_code=404, detail="Feature Flag not found")
    return flag


@router.put("/{flag_id}", response_model=FeatureFlagResponse)
def update(flag_id: int, flag: FeatureFlagUpdate, db: Session = Depends(get_db)):
    updated_flag = feature_flag_service.update_flag(db, flag_id, flag)
    if not updated_flag:
        raise HTTPException(status_code=404, detail="Feature Flag not found")
    return updated_flag


@router.delete("/{flag_id}")
def delete(flag_id: int, db: Session = Depends(get_db)):
    deleted_flag = feature_flag_service.delete_flag(db, flag_id)
    if not deleted_flag:
        raise HTTPException(status_code=404, detail="Feature Flag not found")
    return {"message": "Feature Flag deleted successfully"}