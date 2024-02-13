from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils import get_db, get_password_hash
from schemas import SchemasUserCreate
from crud import create_user, delete_user, update_user, get_user, get_current_user


router_user = APIRouter(tags=["用户路由"])

init_user_data: SchemasUserCreate = SchemasUserCreate(
    username="admin",
    hashed_password="123456",
    job_number="001",
    permission=2,
)


@router_user.get("/init_user", summary="初始化用户", response_model=SchemasUserCreate)
async def init_user(db: Session = Depends(get_db)):
    return create_user(db=db, user_data=init_user_data)


@router_user.post("/create_user", summary="创建用户", response_model=SchemasUserCreate)
async def user_create(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    user: SchemasUserCreate = None,
):

    return create_user(db=db, user_data=user)


@router_user.delete("/delete_user", summary="删除用户")
async def user_delete(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    user_id: int = None,
):
    return delete_user(db=db, user_id=user_id)


@router_user.put("/update_user", summary="更新用户")
async def user_update(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    user_id: int = None,
    user: SchemasUserCreate = None,
):
    return update_user(db=db, user_id=user_id, user_data=user)


@router_user.get("/get_user", summary="获取用户")
async def user_get(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    user_id: int = None,
):
    return get_user(db=db, user_id=user_id)
