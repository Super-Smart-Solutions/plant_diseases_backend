"""
Defines Pydantic models for representing disease data.

This module provides Pydantic models for creating, updating, and representing disease data.
It includes base, create, update, and response schemas.

Attributes:
    DiseaseBaseSchema (BaseModel): Base schema with common disease attributes.
    DiseaseCreateSchema (DiseaseBaseSchema): Schema for creating a new disease.
    DiseaseUpdateSchema (BaseModel): Schema for updating an existing disease.
    DiseaseResponseSchema (DiseaseBaseSchema): Schema for representing a disease response.
"""  # noqa: E501

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DiseaseBaseSchema(BaseModel):
    """Base schema for disease data."""

    name: str
    symptoms: Optional[str] = None
    treatment: Optional[str] = None


class DiseaseCreateSchema(DiseaseBaseSchema):
    """Schema for creating a new disease."""


class DiseaseUpdateSchema(BaseModel):
    """Schema for updating an existing disease."""

    name: Optional[str] = None
    symptoms: Optional[str] = None
    treatment: Optional[str] = None


class DiseaseResponseSchema(DiseaseBaseSchema):
    """Schema for representing a disease response."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
