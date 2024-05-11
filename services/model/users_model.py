from sqlalchemy import (
    Column, String, Integer,
    BigInteger, DateTime, Text
)

from datetime import datetime

from utils import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    username = Column(String(50))
    email = Column(String(60))
    password = Column(Text)
    role = Column(String(20))
    create_at = Column(DateTime, default=datetime.now())