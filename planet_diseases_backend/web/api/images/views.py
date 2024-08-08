"""
API router for managing ImageData entities.

Provides endpoints for creating, reading, updating, and deleting image data.
"""

from fastapi import APIRouter, Depends, HTTPException, status

from planet_diseases_backend.db.dao.image_dao import ImageDAO
from planet_diseases_backend.web.api.images.schema import (
    ImageCreateSchema,
    ImageResponseSchema,
    ImageUpdateSchema,
)

router = APIRouter()


@router.get("/", response_model=list[ImageResponseSchema])
async def retrieve_all_image_data(
    image_data_dao: ImageDAO = Depends(),
) -> list[ImageResponseSchema]:
    """Retrieves a list of all image data.

    Args:
        image_data_dao (Image, Depends): Injected dependency providing access to the Image.

    Returns:
        list[ImageResponseSchema]: A list of all image data objects.
    """  # noqa: E501
    image_data = await image_data_dao.get_all()
    return [ImageResponseSchema.model_validate(img_data) for img_data in image_data]


@router.post("/", response_model=ImageResponseSchema)
async def create_image_data(
    new_image: ImageCreateSchema,
    image_dao: ImageDAO = Depends(),
) -> ImageResponseSchema:
    """Creates a new image data record.

    Args:
    new_image (ImageCreateSchema): The data for the new image.
    image_dao (ImageDAO, Depends): Injected dependency providing access to the ImageDAO.

    Returns:
        ImageResponseSchema: The newly created image details.

    Raises:
        HTTPException: 500 Internal Server Error if creation fails.
    """
    image = await image_dao.add(new_image)
    return ImageResponseSchema.model_validate(image)


@router.get("/{image_id}", response_model=ImageResponseSchema)
async def retrieve_image(
    image_id: int,
    image_dao: ImageDAO = Depends(),
) -> ImageResponseSchema:
    """Retrieves an image by its ID.

    Args:
        image_id (int): The ID of the image to retrieve.
        image_dao (ImageDAO, Depends): Injected dependency providing access to the ImageDAO.

    Returns:
        ImageResponseSchema: The retrieved image details.

    Raises:
        HTTPException: 404 Not Found if the image is not found.
    """  # noqa: E501
    image = await image_dao.get_by_id(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return ImageResponseSchema.model_validate(image)


@router.put("/{image_id}")
async def update_image(
    image: ImageUpdateSchema,
    image_id: int,
    image_dao: ImageDAO = Depends(),
) -> None:
    """Updates an existing image record.

    Args:
    image (ImageUpdateSchema): The updated data for the image.
    image_id (int): The ID of the image to update.
    image_dao (ImageDAO, Depends): Injected dependency providing access to the ImageDAO.

    Returns:
        ImageResponseSchema: The updated image details.

    Raises:
        HTTPException: 404 Not Found if the image is not found.
    """
    return await image_dao.update(image_id, image)


@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_image(
    image_id: int,
    image_dao: ImageDAO = Depends(),
) -> None:
    """Deletes an image by its ID.

    Args:
    image_id (int): The ID of the image to delete.
    image_dao (ImageDAO, Depends): Injected dependency providing access to the ImageDAO.

    Returns:
        None.

    Raises:
        HTTPException: 404 Not Found if the image is not found.
    """
    existing_image = await image_dao.get_by_id(image_id)
    if not existing_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return await image_dao.delete(image_id)
