from fastapi import APIRouter

from .v1 import router_user
from .v1 import router_login
from .v1 import router_computer_room
from .v1 import router_origin_class
from .v1 import router_main_class
from .v1 import router_extension

v1 = APIRouter(prefix="/v1")

v1.include_router(router_user)
v1.include_router(router_login)
v1.include_router(router_computer_room)
v1.include_router(router_origin_class)
v1.include_router(router_main_class)
v1.include_router(router_extension)
