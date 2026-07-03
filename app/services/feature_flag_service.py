from sqlalchemy.orm import Session
from app.models.models import FeatureFlag
from app.schemas.feature_flag import FeatureFlagCreate, FeatureFlagUpdate


def create_flag(db: Session, flag: FeatureFlagCreate):
    db_flag = FeatureFlag(**flag.model_dump())
    db.add(db_flag)
    db.commit()
    db.refresh(db_flag)
    return db_flag


def get_flags(db: Session):
    return db.query(FeatureFlag).all()


def get_flag(db: Session, flag_id: int):
    return db.query(FeatureFlag).filter(FeatureFlag.id == flag_id).first()


def update_flag(db: Session, flag_id: int, flag: FeatureFlagUpdate):
    db_flag = db.query(FeatureFlag).filter(FeatureFlag.id == flag_id).first()

    if not db_flag:
        return None

    update_data = flag.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_flag, key, value)

    db.commit()
    db.refresh(db_flag)
    return db_flag


def delete_flag(db: Session, flag_id: int):
    db_flag = db.query(FeatureFlag).filter(FeatureFlag.id == flag_id).first()

    if not db_flag:
        return None

    db.delete(db_flag)
    db.commit()
    return db_flag