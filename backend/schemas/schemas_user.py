from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str
    empno: str
    role: str


class UserInInfo(UserIn):
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "root",
                "password": "123456",
                "empno": "66668888",
                "role": "0"
            }
        }
