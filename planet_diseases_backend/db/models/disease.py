from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from planet_diseases_backend.db.base import Base

# Association table (Many-to-Many relationship between Diseases and Crops)
disease_crop_association = Table(
    "disease_crop",
    Base.metadata,
    Column("disease_id", Integer, ForeignKey("diseases.id")),
    Column("crop_id", Integer, ForeignKey("crops.id")),
)


class Disease(Base):
    """Represents a plant disease entity in the database."""

    __tablename__ = "diseases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    symptoms = Column(String, nullable=True)
    treatment = Column(String, nullable=True)
    affected_crops = relationship(
        "Crop",
        secondary=disease_crop_association,
        back_populates="diseases",
    )
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Disease(id={self.id}, name='{self.name}', symptoms='{self.symptoms}',\
            treatment='{self.treatment}')>"
