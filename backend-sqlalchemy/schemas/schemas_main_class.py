from typing import List, Optional
from pydantic import BaseModel


class MainClassIn(BaseModel):
    teacherName: str
    teacherRoom: str
    courseName: str
    className: str
    population: str
    software: str
    computerRoomName: str
    lesson: str
    cycle: str


class MainClassJsonIn(BaseModel):
    data: List[MainClassIn]


class UpadateMainClassIn(BaseModel):
    teacherName: str | None = None
    teacherRoom: str | None = None
    courseName: str | None = None
    className: str | None = None
    population: str | None = None
    software: str | None = None
    computerRoomName: str | None = None
    lesson: str | None = None
    cycle: str | None = None
    reTeacherName: str | None = None
    reTeacherRoom: str | None = None
    reCourseName: str | None = None
    reClassName: str | None = None
    rePopulation: str | None = None
    reSoftware: str | None = None
    reComputerRoomName: str | None = None
    reLesson: str | None = None
    reCycle: str | None = None
