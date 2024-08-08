"""
Defines Pydantic models for representing crop data.

This module provides Pydantic models for creating, updating, and representing crop data.
It includes base, create, update, and response schemas.

Attributes:
    CropBaseSchema (BaseModel): Base schema with common crop attributes.
    CropCreateSchema (CropBaseSchema): Schema for creating a new crop.
    CropUpdateSchema (BaseModel): Schema for updating an existing crop.
    CropResponseSchema (CropBaseSchema): Schema for representing a crop response.
"""

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CropBaseSchema(BaseModel):
    """Base schema for crop data."""

    name: str
    variety: Optional[str] = None
    planting_date: Optional[date] = None
    harvest_date: Optional[date] = None
    farm_id: int


class CropCreateSchema(CropBaseSchema):
    """Schema for creating a new crop."""


class CropUpdateSchema(BaseModel):
    """Schema for updating an existing crop."""

    name: Optional[str] = None
    variety: Optional[str] = None
    planting_date: Optional[date] = None
    harvest_date: Optional[date] = None
    farm_id: Optional[int] = None


class CropResponseSchema(CropBaseSchema):
    """Schema for representing a crop response."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
