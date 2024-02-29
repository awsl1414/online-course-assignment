from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils import get_db
from crud import (
    get_current_user,
    create_origin_class,
    delete_origin_class,
    update_origin_class,
    get_origin_class_by_field,
    get_origin_class_all,
)
from schemas import SchemasOriginClassCreate, SchemasOriginClassUpdate


router_origin_class = APIRouter(tags=["原始课程路由"])


@router_origin_class.post(
    "/create_origin_class",
    summary="创建原始课程",
    response_model=SchemasOriginClassCreate,
)
async def origin_class_create(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    origin_class: SchemasOriginClassCreate = None,
):
    return create_origin_class(db=db, origin_class_data=origin_class)


@router_origin_class.delete("/delete_origin_class", summary="删除原始课程")
async def origin_class_delete(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    origin_class_id: int = None,
):
    return delete_origin_class(db=db, origin_class_id=origin_class_id)


@router_origin_class.put("/update_origin_class", summary="更新原始课程")
async def origin_class_update(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    origin_class_id: int = None,
    origin_class: SchemasOriginClassUpdate = None,
):
    return update_origin_class(
        db=db, origin_class_id=origin_class_id, origin_class_data=origin_class
    )


@router_origin_class.get("/get_origin_class_by_field", summary="根据字段获取原始课程")
async def origin_class_get_by_field(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    field_name: str = None,
    value: str = None,
):
    return get_origin_class_by_field(db=db, field_name=field_name, value=value)


@router_origin_class.get("/get_origin_class_all", summary="获取所有原始课程")
async def origin_class_get_all(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_origin_class_all(db=db)
