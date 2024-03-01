from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils import get_db, get_current_user
from crud import (
    create_main_class,
    delete_main_class,
    update_main_class,
    get_main_class_by_field,
    get_main_class_all,
)
from schemas import SchemasMainClassCreate, SchemasMainClassUpdate

router_main_class = APIRouter(tags=["主课程路由"])


@router_main_class.post(
    "/create_main_class", summary="创建主课程", response_model=SchemasMainClassCreate
)
async def main_class_create(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    main_class: SchemasMainClassCreate = None,
):
    return create_main_class(db=db, main_class_data=main_class)


@router_main_class.delete("/delete_main_class", summary="删除主课程")
async def main_class_delete(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    main_class_id: int = None,
):
    return delete_main_class(db=db, main_class_id=main_class_id)


@router_main_class.put("/update_main_class", summary="更新主课程")
async def main_class_update(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    main_class_id: int = None,
    main_class: SchemasMainClassUpdate = None,
):
    return update_main_class(
        db=db, main_class_id=main_class_id, main_class_data=main_class
    )


@router_main_class.get("/get_main_class_by_field", summary="根据字段获取主课程")
async def main_class_get_by_field(
    field_name: str,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    value: str = None,
):
    return get_main_class_by_field(db=db, field_name=field_name, value=value)


@router_main_class.get("/get_main_class_all", summary="获取所有主课程")
async def main_class_get_all(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_main_class_all(db=db)
