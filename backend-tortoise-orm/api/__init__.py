from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from .v1 import v1
from core import settings
from models import User, OriginClass, FinalClass

app = FastAPI(title=settings.TITLE, description=settings.DESC)

app.include_router(v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_tortoise(
    app,
    db_url=settings.DATABASE_URI,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
