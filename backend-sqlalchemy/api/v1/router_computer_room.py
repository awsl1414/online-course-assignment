from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session

from core import get_db
from crud import get_computer_room_software, get_computer_room_floor

from schemas import Response200, Response400, OriginClassIn

router_computer_room = APIRouter(tags=["机房相关"])


@router_computer_room.get("/get_computer_room_software", summary="机房软件查询")
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
    results = {"software": item[0] for item in result}
    results.update({"code": 200, "msg": "请求成功"})
    return results


@router_computer_room.get("/get_computer_room_floor", summary="机房楼层相关查询")
def get_computer_room_floor_api(db: Session = Depends(get_db)):
    result = get_computer_room_floor(db=db)
    return {"code": 200, "msg": "请求成功", "floor": result}
