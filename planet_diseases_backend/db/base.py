from sqlalchemy.orm import DeclarativeBase

from planet_diseases_backend.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
