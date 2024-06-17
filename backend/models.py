from sqlalchemy import Column, String, Integer, DateTime
from database import Base
from datetime import datetime

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True, nullable=False)
    short_url = Column(String, index=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

