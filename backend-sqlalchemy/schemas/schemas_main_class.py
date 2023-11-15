from typing import List, Optional
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


class MainClassJsonIn(BaseModel):
    data: List[MainClassIn]


class UpadateMainClassIn(BaseModel):
    teacherName: str | None = None
    teacherRoom: str | None = None
    courseName: str | None = None
    className: str | None = None
    population: int | None = None
    software: str | None = None
    computerRoomName: str | None = None
    week: int | None = None
    weekDay: int | None = None
    lesson: str | None = None
    littleLesson: str | None = None
    cycle: str | None = None
    reTeacherName: str | None = None
    reTeacherRoom: str | None = None
    reCourseName: str | None = None
    reClassName: str | None = None
    rePopulation: int | None = None
    reSoftware: str | None = None
    reComputerRoomName: str | None = None
    reWeek: int | None = None
    reWeekDay: int | None = None
    reLesson: str | None = None
    reLittleLesson: str | None = None
    reCycle: str | None = None


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
