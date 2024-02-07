from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import settings, init_db

app = FastAPI(title=settings.TITLE, description=settings.DESC)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    init_db()
    run("main:app", host="0.0.0.0", port=80)
