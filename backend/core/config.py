import os
import secrets
from typing import Optional

from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    TITLE: Optional[str] = "网络排课系统"

    DESC: Optional[
        str
    ] = """
    - 实现： 
        前端：Vue
        后端：Fastapi 
    """
    SQLALCHEMY_DATABASE_URI: str = (
        f"sqlite:///{os.path.join(BASE_DIR, '../sql_app.db')}"
    )
    # JWT
    # token相关
    ALGORITHM: str = "HS256"  # 加密算法
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3

    ORIGINS = [
        "http://localhost:5173",  # 这是您的前端开发服务器的地址，您可以根据需要进行修改\
        "http://172.19.219.128:5000",
        "http://172.19.219.127:5000",
        "http://0.0.0.0:5000",
        "*",
    ]


settings = Settings()
