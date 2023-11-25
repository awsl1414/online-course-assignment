"""
create app
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .v1 import v1
from core import (
    settings,
    insert_main_courses_from_json,
    insert_origin_courses_from_json,
    get_db,
)


app = FastAPI(title=settings.TITLE, description=settings.DESC)


def init_db():
    from core import Base, engine
    from models import MainClass, OriginClass, Software, User

    Base.metadata.create_all(bind=engine)

    db = next(get_db())  # 获取数据库session
    try:
        insert_main_courses_from_json(db)
        insert_origin_courses_from_json(db)
    finally:
        db.close()


app.include_router(v1, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
