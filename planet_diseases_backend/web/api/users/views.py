from fastapi import APIRouter, Depends, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from planet_diseases_backend.db.dependencies import get_db_session
from planet_diseases_backend.db.models.users import (
    User,
    UserCreate,
    UserRead,
    UserUpdate,
    api_users,
    auth_jwt,
)

router = APIRouter()

test_router = APIRouter()


@test_router.get(
    "/",
)
async def get_user_models(
    response: Response,
    limit: int = 10,
    offset: int = 0,
    db: AsyncSession = Depends(get_db_session),
) -> list[User]:
    """
    Retrieve a list of user models from the database.

    Args:
        response (Response): The HTTP response object, used to set response headers.
        limit (int, optional): The maximum number of users to retrieve. Defaults to 10.
        offset (int, optional): The number of user models to skip. Defaults to 0.
        db (AsyncSession, optional): The database session dependency.

    Returns:
        List[User]: A list of user models.
    """
    result = await db.execute(select(User).offset(offset).limit(limit))
    users = result.scalars().all()
    response.headers["X-Total-Count"] = str(len(users))
    return list(users)


router.include_router(
    api_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    api_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    api_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    api_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
router.include_router(
    api_users.get_auth_router(auth_jwt),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(test_router, prefix="/users", tags=["users"])
