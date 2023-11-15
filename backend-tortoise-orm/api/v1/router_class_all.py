from fastapi import APIRouter

router_class_all = APIRouter()


@router_class_all.get("/all_test", summary="all_test")
async def test():
    return {"msg": "test"}
