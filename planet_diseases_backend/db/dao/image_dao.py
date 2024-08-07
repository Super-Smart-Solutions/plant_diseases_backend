from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from planet_diseases_backend.db.dao.base_dao import BaseDAO
from planet_diseases_backend.db.dependencies import get_db_session
from planet_diseases_backend.db.models.image import Image


class ImageDAO(BaseDAO[Image]):
    """
    Data Access Object (DAO) for managing Image entities in the database.

    This class inherits from the `BaseDAO` class and provides specific methods
    for interacting with Image data.

    Attributes:
        session (AsyncSession): An injected dependency providing the database session.
    """

    def __init__(self, session: AsyncSession = Depends(get_db_session)) -> None:
        super().__init__(session, Image)
