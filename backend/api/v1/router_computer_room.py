from typing import Optional, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import get_current_user
from utils import get_db
from crud import (
    create_computer_room,
    delete_computer_room,
    update_computer_room,
    get_computer_room_by_field,
)
from schemas import SchemasComputerRoomCreate

router_computer_room = APIRouter(tags=["机房路由"])


@router_computer_room.post(
    "/create_computer_room",
    summary="创建机房",
    response_model=SchemasComputerRoomCreate,
)
async def computer_room_create(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    computer_room: SchemasComputerRoomCreate = None,
):
    return create_computer_room(db=db, computer_room_data=computer_room)


@router_computer_room.delete("/delete_computer_room", summary="删除机房")
async def computer_room_delete(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    computer_room_id: int = None,
):
    return delete_computer_room(db=db, computer_room_id=computer_room_id)


@router_computer_room.put("/update_computer_room", summary="更新机房")
async def computer_room_update(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    computer_room_id: int = None,
    computer_room: SchemasComputerRoomCreate = None,
):
    return update_computer_room(
        db=db, computer_room_id=computer_room_id, computer_room_data=computer_room
    )


@router_computer_room.get("/get_computer_room_by_field", summary="根据字段获取机房")
async def computer_room_get_by_field(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    field_name: str = None,
    value: Any = None,
):
    return get_computer_room_by_field(db=db, field_name=field_name, value=value)
