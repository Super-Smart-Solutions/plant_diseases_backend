from fastapi.routing import APIRouter

from planet_diseases_backend.web.api import (
    crops,
    diseases,
    docs,
    echo,
    farms,
    images,
    monitoring,
    users,
)

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(users.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(farms.router, prefix="/farms", tags=["farms"])
api_router.include_router(crops.router, prefix="/crops", tags=["crops"])
api_router.include_router(diseases.router, prefix="/diseases", tags=["diseases"])
api_router.include_router(images.router, prefix="/images", tags=["images"])
