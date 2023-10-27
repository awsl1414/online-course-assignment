"""
create app
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .v1 import v1
from core import settings


app = FastAPI(title=settings.TITLE, description=settings.DESC)


def init_db():
    from core import Base, engine
    from models import Main, Origin, Software, User

    Base.metadata.create_all(bind=engine)


app.include_router(v1, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
