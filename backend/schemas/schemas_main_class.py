from typing import List
from pydantic import BaseModel


class MainClassIn(BaseModel):
    teacherName: str
    teacherRoom: str
    courseName: str
    className: str
    population: int
    software: str
    computerRoomName: str
    week: int
    weekDay: int
    lesson: str
    littleLesson: str
    cycle: str
