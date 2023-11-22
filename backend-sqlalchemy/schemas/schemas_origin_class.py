from pydantic import BaseModel


class OriginClassIn(BaseModel):
    teacherName: str
    teacherRoom: str
    courseName: str
    className: str
    population: str
    software: str
    week: str

    class Config:
        from_attributes = True


class UpadateOriginClassIn(BaseModel):
    teacherName: str | None = None
    teacherRoom: str | None = None
    courseName: str | None = None
    className: str | None = None
    population: str | None = None
    software: str | None = None
    week: str | None = None
    reTeacherName: str | None = None
    reTeacherRoom: str | None = None
    reCourseName: str | None = None
    reClassName: str | None = None
    rePopulation: str | None = None
    reSoftware: str | None = None
    reWeek: str | None = None
