"""
Defines Pydantic models for representing image .

This module provides Pydantic models for creating, updating, and representing image .
It includes base, create, update, and response schemas.

Attributes:
    ImageBaseSchema (BaseModel): Base schema with common image  attributes.
    ImageCreateSchema (ImageBaseSchema): Schema for creating a new image.
    ImageUpdateSchema (BaseModel): Schema for updating an existing image.
    ImageResponseSchema (ImageBaseSchema): Schema for representing an image response.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ImageBaseSchema(BaseModel):
    """Base schema for image ."""

    image_url: str
    description: Optional[str] = None
    farm_id: Optional[int] = None
    crop_id: Optional[int] = None
    disease_id: Optional[int] = None


class ImageCreateSchema(ImageBaseSchema):
    """Schema for creating a new image."""


class ImageUpdateSchema(BaseModel):
    """Schema for updating an existing image."""

    image_url: Optional[str] = None
    description: Optional[str] = None
    farm_id: Optional[int] = None
    crop_id: Optional[int] = None
    disease_id: Optional[int] = None


class ImageResponseSchema(ImageBaseSchema):
    """Schema for representing an image response."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
