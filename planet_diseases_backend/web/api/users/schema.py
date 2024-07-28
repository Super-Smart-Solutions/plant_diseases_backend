"""
This module defines the UserResponseModel Pydantic model used for
serializing and validating user data in API responses.
"""  # noqa: D205

from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UserResponseModel(BaseModel):
    """
    UserResponseModel represents the response schema for user data in the API.

    Attributes:
        id (UUID): The unique identifier of the user.
        email (str): The email address of the user.
        is_active (bool): Indicates whether the user's account is active.
        is_verified (bool): Indicates whether the user's email has been verified.
        is_superuser (bool): Indicates whether the user has superuser privileges.
    """

    id: UUID
    email: str
    is_active: bool
    is_verified: bool
    is_superuser: bool

    model_config = ConfigDict(from_attributes=True)
