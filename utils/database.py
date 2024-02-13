from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=False,  # echo 设为 True 会打印出实际执行的 sql，调试的时候更方便
    future=True,  # 使用 SQLAlchemy 2.0 API，向后兼容
    pool_size=5,  # 连接池的大小默认为 5 个，设置为 0 时表示连接无限制
    pool_recycle=3600,  # 设置时间以限制数据库自动断开
    # 创建一个 SQLite 的内存数据库，必须加上 check_same_thread=False，否则无法在多线程中使用
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()


def init_db():

    from models import (
        ModelsComputerRoom,
        ModelsMainClass,
        ModelsOriginClass,
        ModelsUser,
    )

    Base.metadata.create_all(bind=engine)
    db = next(get_db())
    try:
        db.commit()
    finally:
        db.close()
