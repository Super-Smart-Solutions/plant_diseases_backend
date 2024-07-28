from fastapi import APIRouter, Depends, Response
from planet_diseases_backend.db.dependencies import get_db_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from planet_diseases_backend.db.models.users import (
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
):
    result = await db.execute(select(User).offset(offset).limit(limit))
    users = result.scalars().all()
    response.headers["X-Total-Count"] = str(len(users))
    return users

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
