"""
Defines Pydantic models for representing farm data.

This module provides Pydantic models for creating, updating, and representing farm data.
It includes base, create, update, and response schemas.

Attributes:
    FarmBaseSchema (BaseModel): Base schema with common farm attributes.
    FarmCreateSchema (FarmBaseSchema): Schema for creating a new farm.
    FarmUpdateSchema (FarmBaseSchema): Schema for updating an existing farm.
    FarmResponseSchema (FarmBaseSchema): Schema for representing a farm response.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FarmBaseSchema(BaseModel):
    """Base schema for farm data."""

    name: str
    location: str
    weather: Optional[str] = None


class FarmCreateSchema(FarmBaseSchema):
    """Schema for creating a new farm."""


class FarmUpdateSchema(BaseModel):
    """Schema for updating an existing farm."""

    name: Optional[str] = None
    location: Optional[str] = None
    weather: Optional[str] = None


class FarmResponseSchema(FarmBaseSchema):
    """Schema for representing a farm response."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
