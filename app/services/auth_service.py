from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.auth import UserSignup, UserLogin


def signup_user(db: Session, user: UserSignup):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(db: Session, user: UserLogin):
    return db.query(User).filter(
        User.email == user.email,
        User.password == user.password
    ).first()