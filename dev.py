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
    run("dev:app", host="127.0.0.1", port=5000, reload=True)


if __name__ == "__main__":
    start_server()
