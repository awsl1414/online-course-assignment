from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import settings, init_db
from api import v1


app = FastAPI(title=settings.TITLE, description=settings.DESC)

app.include_router(v1, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start_server():
    init_db()
    run("main:app", host="0.0.0.0", port=5000)


if __name__ == "__main__":
    start_server()
