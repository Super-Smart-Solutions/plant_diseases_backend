"""
API router for managing Crop entities.

Provides endpoints for creating, reading, updating, and deleting crops.
"""

from fastapi import APIRouter, Depends, HTTPException, status

from planet_diseases_backend.db.dao.crop_dao import CropDAO
from planet_diseases_backend.web.api.crops.schema import (
    CropCreateSchema,
    CropResponseSchema,
    CropUpdateSchema,
)

router = APIRouter()


@router.get("/", response_model=list[CropResponseSchema])
async def retrieve_all_crops(
    crop_dao: CropDAO = Depends(),
) -> list[CropResponseSchema]:
    """Retrieves a list of all crops.

    Args:
        crop_dao (CropDAO, Depends): Injected dependency providing access to the CropDAO.

    Returns:
        list[CropResponseSchema]: A list of all crop objects.
    """  # noqa: E501
    crops = await crop_dao.get_all()
    return [CropResponseSchema.model_validate(crop) for crop in crops]


@router.post("/", response_model=CropResponseSchema)
async def create_crop(
    new_crop: CropCreateSchema,
    crop_dao: CropDAO = Depends(),
) -> CropResponseSchema:
    """Creates a new crop record.

    Args:
        new_crop (CropCreateSchema): The data for the new crop.
        crop_dao (CropDAO, Depends): Injected dependency providing access to the CropDAO.

    Returns:
        CropResponseSchema: The newly created crop details.

    Raises:
        HTTPException: 500 Internal Server Error if creation fails.
    """  # noqa: E501
    crop = await crop_dao.add(new_crop)
    return CropResponseSchema.model_validate(crop)


@router.get("/{crop_id}", response_model=CropResponseSchema)
async def retrieve_crop(
    crop_id: int,
    crop_dao: CropDAO = Depends(),
) -> CropResponseSchema:
    """Retrieves a crop by its ID.

    Args:
        crop_id (int): The ID of the crop to retrieve.
        crop_dao (CropDAO, Depends): Injected dependency providing access to the CropDAO.

    Returns:
        CropResponseSchema: The retrieved crop details.

    Raises:
        HTTPException: 404 Not Found if the crop is not found.
    """  # noqa: E501
    crop = await crop_dao.get_by_id(crop_id)
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")
    return CropResponseSchema.model_validate(crop)


@router.put("/{crop_id}")
async def update_crop(
    crop: CropUpdateSchema,
    crop_id: int,
    crop_dao: CropDAO = Depends(),
) -> None:
    """Updates an existing crop record.

    Args:
        crop (CropUpdateSchema): The updated data for the crop.
        crop_id (int): The ID of the crop to update.
        crop_dao (CropDAO, Depends): Injected dependency providing access to the CropDAO.

    Returns:
        CropResponseSchema: The updated crop details.

    Raises:
        HTTPException: 404 Not Found if the crop is not found.
    """  # noqa: E501
    return await crop_dao.update(crop_id, crop)


@router.delete("/{crop_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_crop(
    crop_id: int,
    crop_dao: CropDAO = Depends(),
) -> None:
    """Deletes a crop by its ID.

    Args:
        crop_id (int): The ID of the crop to delete.
        crop_dao (CropDAO, Depends): Injected dependency providing access to the CropDAO.

    Returns:
        None

    Raises:
        HTTPException: 404 Not Found if the crop is not found.
    """  # noqa: E501
    existing_crop = await crop_dao.get_by_id(crop_id)
    if not existing_crop:
        raise HTTPException(status_code=404, detail="Crop not found")
    return await crop_dao.delete(crop_id)
