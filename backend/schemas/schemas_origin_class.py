from pydantic import BaseModel


class OriginClassIn(BaseModel):
    teacherName: str
    courseName: str
    className: str
    classroomName: str
    population: int


class OriginClass(BaseModel):
    teacherName: str
    courseName: str
    className: str
    population: int
    software: str
    cycle: str

    class Config:
        from_attributes = True


class OriginClassIn(OriginClass):
    pass
