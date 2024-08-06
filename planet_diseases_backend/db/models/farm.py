from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from planet_diseases_backend.db.base import Base


class Farm(Base):
    """Represents a farm entity in the database."""

    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    weather = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Farm(id={self.id}, name='{self.name}', location='{self.location}',\
            weather='{self.weather}')>"
