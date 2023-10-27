from pydantic import BaseModel


class MainIn(BaseModel):
    teacherName: str
    courseName: str
    className: str
    classroomName: str
    week: int
    weekDay: int
    section: int
    population: int
    software: str
    measure: str


class OriginIn(BaseModel):
    teacherName: str
    courseName: str
    className: str
    classroomName: str
    population: int
    software: str


class UserIn(BaseModel):
    username: str
    empno: int
    password: int
    role: str


class UserInInfo(UserIn):
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {"username": "root", "password": "123456", "role": "0"}
        }
