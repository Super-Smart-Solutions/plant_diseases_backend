"""
API router for managing Disease entities.

Provides endpoints for creating, reading, updating, and deleting diseases.
"""

from fastapi import APIRouter, Depends, HTTPException, status

from planet_diseases_backend.db.dao.disease_dao import DiseaseDAO
from planet_diseases_backend.web.api.diseases.schema import (
    DiseaseCreateSchema,
    DiseaseResponseSchema,
    DiseaseUpdateSchema,
)

router = APIRouter()


@router.get("/", response_model=list[DiseaseResponseSchema])
async def retrieve_all_diseases(
    disease_dao: DiseaseDAO = Depends(),
) -> list[DiseaseResponseSchema]:
    """Retrieves a list of all diseases.

    Args:
        disease_dao (DiseaseDAO, Depends): Injected dependency providing access to the DiseaseDAO.

    Returns:
        list[DiseaseResponseSchema]: A list of all disease objects.
    """  # noqa: E501
    diseases = await disease_dao.get_all()
    return [DiseaseResponseSchema.model_validate(disease) for disease in diseases]


@router.post("/", response_model=DiseaseResponseSchema)
async def create_disease(
    new_disease: DiseaseCreateSchema,
    disease_dao: DiseaseDAO = Depends(),
) -> DiseaseResponseSchema:
    """Creates a new disease record.

    Args:
        new_disease (DiseaseCreateSchema): The data for the new disease.
        disease_dao (DiseaseDAO, Depends): Injected dependency providing access to the DiseaseDAO.

    Returns:
        DiseaseResponseSchema: The newly created disease details.

    Raises:
        HTTPException: 500 Internal Server Error if creation fails.
    """  # noqa: E501
    disease = await disease_dao.add(new_disease)
    return DiseaseResponseSchema.model_validate(disease)


@router.get("/{disease_id}", response_model=DiseaseResponseSchema)
async def retrieve_disease(
    disease_id: int,
    disease_dao: DiseaseDAO = Depends(),
) -> DiseaseResponseSchema:
    """Retrieves a disease by its ID.

    Args:
        disease_id (int): The ID of the disease to retrieve.
        disease_dao (DiseaseDAO, Depends): Injected dependency providing access to the DiseaseDAO.

    Returns:
        DiseaseResponseSchema: The retrieved disease details.

    Raises:
        HTTPException: 404 Not Found if the disease is not found.
    """  # noqa: E501
    disease = await disease_dao.get_by_id(disease_id)
    if not disease:
        raise HTTPException(status_code=404, detail="Disease not found")
    return DiseaseResponseSchema.model_validate(disease)


@router.put("/{disease_id}")
async def update_disease(
    disease: DiseaseUpdateSchema,
    disease_id: int,
    disease_dao: DiseaseDAO = Depends(),
) -> None:
    """Updates an existing disease record.

    Args:
        disease (DiseaseUpdateSchema): The updated data for the disease.
        disease_id (int): The ID of the disease to update.
        disease_dao (DiseaseDAO, Depends): Injected dependency providing access to the DiseaseDAO.

    Returns:
        DiseaseResponseSchema: The updated disease details.

    Raises:
        HTTPException: 404 Not Found if the disease is not found.
    """  # noqa: E501
    return await disease_dao.update(disease_id, disease)


@router.delete("/{disease_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_disease(
    disease_id: int,
    disease_dao: DiseaseDAO = Depends(),
) -> None:
    """Deletes a disease by its ID.

    Args:
        disease_id (int): The ID of the disease to delete.
        disease_dao (DiseaseDAO, Depends): Injected dependency providing access to the DiseaseDAO.

    Returns:
        None

    Raises:
        HTTPException: 404 Not Found if the disease is not found.
    """  # noqa: E501
    existing_disease = await disease_dao.get_by_id(disease_id)
    if not existing_disease:
        raise HTTPException(status_code=404, detail="Disease not found")
    return await disease_dao.delete(disease_id)
