from app.models.base import base
from sqlalchemy import String, Boolean, Column, Enum
from enum import Enum as PyEnum

class UserRole(str, PyEnum):
    ADMIN = "admin"
    STOREKEEPER = "storekeeper"
    WOEKER = "worker"


class User(base):
    __tablename__ = "users"

    login = Column(String(64), unique=True, index=True, nullable=False),
    password_hash = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    telegramm_username = Column(String(64), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False)
    