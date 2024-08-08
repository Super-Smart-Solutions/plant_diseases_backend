from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from planet_diseases_backend.db.base import Base


class Image(Base):
    """Represents an image entity in the database."""

    __tablename__ = "image"

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    farm_id = Column(Integer, ForeignKey("farms.id"), nullable=True)
    crop_id = Column(Integer, ForeignKey("crops.id"), nullable=True)
    disease_id = Column(Integer, ForeignKey("diseases.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ImageData(id={self.id}, image_url='{self.image_url}',\
            description='{self.description}', farm_id={self.farm_id},\
                crop_id={self.crop_id}, disease_id={self.disease_id})>"
