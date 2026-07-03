from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.schemas.environment import (
    EnvironmentCreate,
    EnvironmentUpdate,
    EnvironmentResponse,
)
from app.services.environment_service import (
    create_environment,
    get_environments,
    get_environment,
    update_environment,
    delete_environment,
)

router = APIRouter()

@router.post("/", response_model=EnvironmentResponse)
def create(environment: EnvironmentCreate, db: Session = Depends(get_db)):
    return create_environment(db, environment)


@router.get("/", response_model=list[EnvironmentResponse])
def read_all(db: Session = Depends(get_db)):
    return get_environments(db)


@router.get("/{environment_id}", response_model=EnvironmentResponse)
def read_one(environment_id: int, db: Session = Depends(get_db)):
    environment = get_environment(db, environment_id)

    if not environment:
        raise HTTPException(status_code=404, detail="Environment not found")

    return environment


@router.put("/{environment_id}", response_model=EnvironmentResponse)
def update(
    environment_id: int,
    environment: EnvironmentUpdate,
    db: Session = Depends(get_db),
):
    updated = update_environment(db, environment_id, environment)

    if not updated:
        raise HTTPException(status_code=404, detail="Environment not found")

    return updated


@router.delete("/{environment_id}")
def delete(environment_id: int, db: Session = Depends(get_db)):
    deleted = delete_environment(db, environment_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Environment not found")

    return {"message": "Environment deleted successfully"}