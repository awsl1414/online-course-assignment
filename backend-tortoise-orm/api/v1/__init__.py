from fastapi import APIRouter
from .router_class_all import router_class_all
from .router_class_origin import router_class_origin
from .router_user import router_class_user

v1 = APIRouter(prefix="/v1")
v1.include_router(router_class_all)
v1.include_router(router_class_origin)
v1.include_router(router_class_user)
