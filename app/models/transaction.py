from app.models.base import base
from sqlalchemy import Integer, String, Boolean, Column, Enum, Date, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import date, datetime
from enum import Enum as PyEnum

class TransactionType(str, PyEnum):
    RECEIPT = "receipt"
    ISSUE = "issue"
    RETURN = "return"
    ADJUSTMENT = "adjustment"
    DISPOSAL = "disposal"

class Transaction(base):
    __tablename__ = "transactions"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False),
    item_id = Column(Integer,ForeignKey("item_types.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    timestamp = Column(Date, default=datetime.now())
    notes = Column(String, ForeignKey("users.id"), nullable=True)

    user = relationship("User")
    item = relationship("Item")