from pydantic import BaseModel


class OriginIn(BaseModel):
    teacherName: str
    courseName: str
    className: str
    classroomName: str
    population: int
