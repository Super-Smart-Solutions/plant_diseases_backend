"""
Defines Pydantic models for representing image data.

This module provides Pydantic models for creating, updating, and representing image data.
It includes base, create, update, and response schemas.

Attributes:
    ImageDataBaseSchema (BaseModel): Base schema with common image data attributes.
    ImageDataCreateSchema (ImageDataBaseSchema): Schema for creating a new image.
    ImageDataUpdateSchema (BaseModel): Schema for updating an existing image.
    ImageDataResponseSchema (ImageDataBaseSchema): Schema for representing an image response.
"""  # noqa: E501

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ImageDataBaseSchema(BaseModel):
    """Base schema for image data."""

    image_url: str
    description: Optional[str] = None
    farm_id: Optional[int] = None
    crop_id: Optional[int] = None
    disease_id: Optional[int] = None


class ImageDataCreateSchema(ImageDataBaseSchema):
    """Schema for creating a new image."""


class ImageDataUpdateSchema(BaseModel):
    """Schema for updating an existing image."""

    image_url: Optional[str] = None
    description: Optional[str] = None
    farm_id: Optional[int] = None
    crop_id: Optional[int] = None
    disease_id: Optional[int] = None


class ImageDataResponseSchema(ImageDataBaseSchema):
    """Schema for representing an image response."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
