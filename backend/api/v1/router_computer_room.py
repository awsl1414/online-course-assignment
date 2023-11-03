from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session

from core import get_db
from crud import get_computer_room_software

from schemas import Response200, Response400, OriginClassIn

router_computer_room = APIRouter(tags=["机房相关"])


@router_computer_room.get("/get_computer_room_software", summary="原始课表查询")
def get_computer_room_software_api(
    db: Session = Depends(get_db),
    computerRoomName: Optional[str] = Query(None),
):
    result = get_computer_room_software(
        db=db,
        computerRoomName=computerRoomName,
    )
    if not result:
        return Response400(msg="无此机房")
    return result
