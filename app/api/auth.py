from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.schemas.auth import UserSignup, UserLogin, UserResponse
from app.services.auth_service import signup_user, login_user

router = APIRouter()


@router.post("/signup", response_model=UserResponse)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    created_user = signup_user(db, user)

    if not created_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    return created_user


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = login_user(db, user)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {"message": "Login Successful"}