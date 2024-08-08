from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from planet_diseases_backend.db.base import Base
from planet_diseases_backend.db.models.disease import disease_crop_association


class Crop(Base):
    """Represents a crop entity in the database."""

    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    variety = Column(String, nullable=True)
    planting_date = Column(Date, nullable=False)
    harvest_date = Column(Date, nullable=True)
    farm_id = Column(Integer, ForeignKey("farms.id"), nullable=False)
    diseases = relationship(
        "Disease",
        secondary=disease_crop_association,
        back_populates="affected_crops",
    )
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Crop(id={self.id}, name='{self.name}', variety='{self.variety}',\
          planting_date='{self.planting_date}', harvest_date='{self.harvest_date}',\
            farm_id={self.farm_id})>"
