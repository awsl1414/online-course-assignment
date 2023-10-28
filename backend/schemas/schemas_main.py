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
