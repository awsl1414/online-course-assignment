from fastapi import APIRouter

from .endpoints import *

v1 = APIRouter(prefix="/v1")

v1.include_router(router_user)
