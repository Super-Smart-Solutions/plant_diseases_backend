from typing import Any, Generic, List, Optional, Type, TypeVar, Union

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from planet_diseases_backend.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class BaseDAO(Generic[ModelType]):
    """
    Base Data Access Object (DAO) for interacting with database models.

    Provides common CRUD operations for generic SQLAlchemy models.

    Args:
        session (AsyncSession): An asynchronous SQLAlchemy session.
        model_class (Type[ModelType]): The SQLAlchemy model class to interact with.

    Attributes:
        session (AsyncSession): The SQLAlchemy session.
        model_class (Type[ModelType]): The SQLAlchemy model class.
    """

    def __init__(self, session: AsyncSession, model_class: Type[ModelType]) -> None:
        self.session = session
        self.model_class = model_class

    async def get_by_id(self, record_id: int) -> Optional[ModelType]:
        """Retrieves a record by its ID.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            Optional[ModelType]: The retrieved record, or None if not found.
        """
        result = await self.session.execute(
            select(self.model_class).filter_by(id=record_id),
        )
        return result.scalars().first()

    async def get_all(self) -> list[ModelType]:
        """Retrieves all records.

        Returns:
            list[ModelType]: A list of all records.
        """
        result = await self.session.execute(select(self.model_class))
        return list(result.scalars().all())

    async def add(self, record: SchemaType) -> ModelType:
        """Adds a record to the database.

        Args:
            record (SchemaType): The Pydantic schema to add.
            model_class (Type[Base]): The SQLAlchemy model class to convert the schema to.

        Returns:
            Base: The added crop.
        """  # noqa: E501
        model_instance = self.model_class(**record.model_dump())
        self.session.add(model_instance)
        await self.session.commit()
        await self.session.refresh(model_instance)
        return model_instance

    async def update(self, record_id: int, updated_record: SchemaType) -> None:
        """Updates a record based on its ID.

        Args:
            record_id (int): The ID of the record to update.
            updated_data (dict): A dictionary containing the updated fields and values.
        """
        query = select(self.model_class).filter_by(id=record_id)
        result = await self.session.execute(query)
        existing_record = result.scalars().first()

        if existing_record:
            for key, value in vars(updated_record).items():
                setattr(existing_record, key, value)
            await self.session.commit()

    async def delete(self, record_id: int) -> None:
        """Deletes a record by its ID.

        Args:
            record_id (int): The ID of the record to delete.
        """
        result = await self.session.execute(
            select(self.model_class).filter_by(id=record_id),
        )
        record = result.scalars().first()
        if record:
            await self.session.delete(record)
            await self.session.commit()

    async def get_by(
        self,
        field: str,
        value: Any,
        unique: bool = False,
    ) -> Union[Optional[ModelType], List[ModelType]]:
        """Retrieves records based on a field and value.

        Args:
            field (str): The name of the field to filter by.
            value (Any): The value to filter for.
            unique (bool): Whether to return a single record or all matching records. Defaults to False.

        Returns:
            Union[Optional[ModelType], List[ModelType]]: The retrieved record(s) or None if not found.
        """  # noqa: E501
        query = select(self.model_class).filter(
            getattr(self.model_class, field) == value,
        )

        result = await self.session.execute(query)
        if unique:
            return result.scalars().first()
        return list(result.scalars().all())
