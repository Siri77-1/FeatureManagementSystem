from sqlalchemy.orm import Session
from app.models.models import Environment
from app.schemas.environment import EnvironmentCreate, EnvironmentUpdate


def create_environment(db: Session, environment: EnvironmentCreate):
    db_environment = Environment(
        name=environment.name,
        description=environment.description
    )
    db.add(db_environment)
    db.commit()
    db.refresh(db_environment)
    return db_environment


def get_environments(db: Session):
    return db.query(Environment).all()


def get_environment(db: Session, environment_id: int):
    return db.query(Environment).filter(Environment.id == environment_id).first()


def update_environment(db: Session, environment_id: int, environment: EnvironmentUpdate):
    db_environment = db.query(Environment).filter(Environment.id == environment_id).first()

    if not db_environment:
        return None

    if environment.name is not None:
        db_environment.name = environment.name

    if environment.description is not None:
        db_environment.description = environment.description

    db.commit()
    db.refresh(db_environment)
    return db_environment


def delete_environment(db: Session, environment_id: int):
    db_environment = db.query(Environment).filter(Environment.id == environment_id).first()

    if not db_environment:
        return None

    db.delete(db_environment)
    db.commit()
    return db_environment