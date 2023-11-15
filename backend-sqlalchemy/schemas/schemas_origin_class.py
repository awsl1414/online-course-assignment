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


class UpadateOriginClassIn(BaseModel):
    teacherName: str | None = None
    teacherRoom: str | None = None
    courseName: str | None = None
    className: str | None = None
    software: str | None = None
    cycle: str | None = None
    reTeacherName: str | None = None
    reTeacherRoom: str | None = None
    reCourseName: str | None = None
    reClassName: str | None = None
    reSoftware: str | None = None
    reCycle: str | None = None
