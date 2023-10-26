from fastapi import APIRouter

router_user = APIRouter(tags=["用户相关"])


@router_user.get("/test")
def test():
    return "test"
