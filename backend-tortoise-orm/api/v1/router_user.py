from fastapi import APIRouter

router_class_user = APIRouter()


@router_class_user.get("/user_test", summary="user_test")
async def test():
    return {"msg": "test"}
