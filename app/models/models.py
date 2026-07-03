from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.database import Base


class Environment(Base):
    __tablename__ = "environments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class FeatureFlag(Base):
    __tablename__ = "feature_flags"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False)
    description = Column(String)
    type = Column(String)
    default_value = Column(String)
    enabled = Column(Boolean, default=True)
    owner_team = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class EnvironmentOverride(Base):
    __tablename__ = "environment_overrides"

    id = Column(Integer, primary_key=True, index=True)
    flag_id = Column(Integer, ForeignKey("feature_flags.id"))
    environment_id = Column(Integer, ForeignKey("environments.id"))
    value = Column(String)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
    performed_by = Column(String)
    old_value = Column(String)
    new_value = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())