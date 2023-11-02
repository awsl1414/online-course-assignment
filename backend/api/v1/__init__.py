from fastapi import APIRouter
from .router_login import router_login
from .router_user import router_user
from .router_course import router_course

v1 = APIRouter(prefix="/v1")

v1.include_router(router_login)
v1.include_router(router_user)
v1.include_router(router_course)
