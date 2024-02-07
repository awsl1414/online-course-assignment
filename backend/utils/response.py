from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    """业务状态码"""

    SUCCESS = 200
    FAIL = 400
    NOT_FOUND = 404


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(
        default=CodeEnum.SUCCESS, description="业务状态码 200 是成功, 400 是失败"
    )
    msg: Any = Field(default=None, description="数据结果")


class Response200(ResponseBasic):
    pass


class ResponseToken(BaseModel):
    access_token: str
    token_type: str


class Response400(ResponseBasic):
    code: CodeEnum = CodeEnum.FAIL
    msg: str = "请求失败"


class Response404(ResponseBasic):
    code: CodeEnum = CodeEnum.NOT_FOUND
    msg: str = "记录未找到"
