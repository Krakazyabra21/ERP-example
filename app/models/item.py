from app.models.base import base
from sqlalchemy import Integer, String, Boolean, Column, Enum, Date, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import date, timedelta
from enum import Enum as PyEnum

class ItemStatus(str, PyEnum):
    IN_STOCK = "in_stock"
    ISSUED = "issued"
    EXPIRED = "expired"
    UNDER_MAINTANCE = "under_maintance"


class ItemType(base):
    __tablename__ = "item_types"

    name = Column(String(64), unique=True, index=True, nullable=False),
    warranty_period = Column(Integer, nullable=False)
    item = relationship("Item", back_populates="type")


class User(base):
    __tablename__ = "items"

    serial_number = Column(String(64), unique=True, nullable=False),
    type_id = Column(Integer,ForeignKey("item_types.id"))
    status = Column(Enum(ItemStatus), default=ItemStatus.IN_STOCK)
    receipt_date = Column(Date, default=date.today)
    issue_date = Column(Date)
    worker_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    expiration_date = Column(Date)

    type= relationship("ItemType", back_populates="items")
    worker = relationship("User")

    @property
    def is_expired(self):
        if self.status != ItemStatus.ISSUED or not self.issue_date:
            return False
        return date.today() > self.expiration_date
    