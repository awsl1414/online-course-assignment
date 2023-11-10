from pydantic import BaseModel


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
