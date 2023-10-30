from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str
    job_number:str
    permission:int


class UserInInfo(UserIn):
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "root",
                "password": "123456",
                "jon_number": "66668888",
                "permission": 2
            }
        }
