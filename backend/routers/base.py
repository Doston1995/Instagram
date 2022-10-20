from fastapi import APIRouter
from routers import user_route


router = APIRouter()

router.include_router(user_route.router,  prefix="/auth",tags=["auths"])