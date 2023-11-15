from fastapi import APIRouter

router_class_origin = APIRouter()


@router_class_origin.get("/origin_test", summary="origin_test")
async def test():
    return {"msg": "test"}
