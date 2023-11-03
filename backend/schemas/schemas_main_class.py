from pydantic import BaseModel


class MainClassIn(BaseModel):
    teacherName: str
    courseName: str
    population: int
    software: str
    classRoomName: str
    week: int
    weekDay: int
    lesson: str
    littleLesson: str
    cycle: str
