from uvicorn import run

from api import app
from core import settings


# 手动初始化
# async def init():
#     await Tortoise.init(
#         db_url=settings.DATABASE_URI,
#         modules={"models": ["models"]},
#     )
#     # 生成schema
#     await Tortoise.generate_schemas()
#     # 在应用关闭时关闭Tortoise连接
#     app.add_event_handler("shutdown", Tortoise.close_connections)
# run_async(init())

# 自动初始化
# register_tortoise(
#     app,
#     db_url=settings.DATABASE_URI,
#     modules={"models": ["models"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )


if __name__ == "__main__":
    # run("main:app", host="0.0.0.0", port=5000, reload=True)
    run("main:app", host="127.0.0.1", port=5000, reload=True)
