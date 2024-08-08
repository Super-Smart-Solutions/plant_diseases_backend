"""
API router for managing Farm entities.

Provides endpoints for creating, reading, updating, and deleting farms.
"""

from fastapi import APIRouter, Depends, HTTPException, status

from planet_diseases_backend.db.dao.farm_dao import FarmDAO
from planet_diseases_backend.web.api.farms.schema import (
    FarmCreateSchema,
    FarmResponseSchema,
    FarmUpdateSchema,
)

router = APIRouter()


@router.get("/", response_model=list[FarmResponseSchema])
async def retrieve_all_farms(
    farm_dao: FarmDAO = Depends(),
) -> list[FarmResponseSchema]:
    """Retrieves a list of all farms.

    Args:
        farm_dao (FarmDAO, Depends): Injected dependency providing access to the FarmDAO.

    Returns:
        list[FarmResponseSchema]: A list of all farm objects.
    """  # noqa: E501
    farms = await farm_dao.get_all()
    return [FarmResponseSchema.model_validate(farm) for farm in farms]


@router.post("/", response_model=FarmResponseSchema)
async def create_farm(
    new_farm: FarmCreateSchema,
    farm_dao: FarmDAO = Depends(),
) -> FarmResponseSchema:
    """Creates a new farm record.

    Args:
        new_farm (FarmCreateSchema): The data for the new farm.
        farm_dao (FarmDAO, Depends): Injected dependency providing access to the FarmDAO.

    Returns:
        FarmResponseSchema: The newly created farm details.

    Raises:
        HTTPException: 500 Internal Server Error if creation fails.
    """  # noqa: E501
    farm = await farm_dao.add(new_farm)
    return FarmResponseSchema.model_validate(farm)


@router.get("/{farm_id}", response_model=FarmResponseSchema)
async def retrieve_farm(
    farm_id: int,
    farm_dao: FarmDAO = Depends(),
) -> FarmResponseSchema:
    """Retrieves a farm by its ID.

    Args:
        farm_id (int): The ID of the farm to retrieve.
        farm_dao (FarmDAO, Depends): Injected dependency providing access to the FarmDAO.

    Returns:
        FarmResponseSchema: The retrieved farm details.

    Raises:
        HTTPException: 404 Not Found if the farm is not found.
    """  # noqa: E501
    farm = await farm_dao.get_by_id(farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return FarmResponseSchema.model_validate(farm)


@router.put("/{farm_id}")
async def update_farm(
    farm: FarmUpdateSchema,
    farm_id: int,
    farm_dao: FarmDAO = Depends(),
) -> None:
    """Updates an existing farm record.

    Args:
        farm (FarmUpdateSchema): The updated data for the farm.
        farm_id (int): The ID of the farm to update.
        farm_dao (FarmDAO, Depends): Injected dependency providing access to the FarmDAO.

    Returns:
        FarmResponseSchema: The updated farm details.

    Raises:
        HTTPException: 404 Not Found if the farm is not found.
    """  # noqa: E501
    return await farm_dao.update(farm_id, farm)


@router.delete("/{farm_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_farm(
    farm_id: int,
    farm_dao: FarmDAO = Depends(),
) -> None:
    """Deletes a farm by its ID.

    Args:
        farm_id (int): The ID of the farm to delete.
        farm_dao (FarmDAO, Depends): Injected dependency providing access to the FarmDAO.

    Returns:
        None

    Raises:
        HTTPException: 404 Not Found if the farm is not found.
    """  # noqa: E501
    existing_farm = await farm_dao.get_by_id(farm_id)
    if not existing_farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return await farm_dao.delete(farm_id)
