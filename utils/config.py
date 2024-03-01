import os
import secrets
from typing import Optional

from pydantic_settings import BaseSettings

# 当前所在的目录
current_path = os.path.dirname(os.path.abspath(__file__))

# 项目目录
BASE_DIR = os.path.dirname(current_path)


class Settings(BaseSettings):
    TITLE: Optional[str] = "网络排课系统"
    DESC: Optional[
        str
    ] = """
    - 实现： 
        前端：Vue3
        后端：Fastapi
        数据库：sqlite
    """

    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{os.path.join(BASE_DIR, 'sql_app.db')}"

    # JWT
    # token相关
    ALGORITHM: str = "HS256"  # 加密算法
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # token的时效 7 天 = 60 * 24 * 7

    ORIGINS: list = [
        "http://localhost:5173",  # 本地前端
        "*",
    ]


settings = Settings()
