from typing import List
from pydantic import BaseModel


class MainClassIn(BaseModel):
    # teacherName: str
    # teacherRoom: str
    # courseName: str
    # className: str
    # population: int
    # software: str
    # computerRoomName: str
    # week: int
    # weekDay: int
    # lesson: str
    # littleLesson: str
    # cycle: str
    data: List[str]

    # class Config:
    #     json_schema_extra = {
    #         "data": [
    #             {
    #                 "teacher_name": "string",
    #                 "course_name": "无人机模拟",
    #                 "population": 0,
    #                 "software": "photoshop",
    #                 "cycle": "1/16",
    #                 "computer_room_name": "C501",
    #                 "week": "1",
    #                 "day": "1",
    #                 "lesson": "1-2",
    #                 "little_lesson": "true",
    #             }
    #         ]
    #     }
    class Config:
        json_schema_extra = {
            "example": {
                "info": ["双能 20 自动化 01 123", "双能 21 机器人 02 456", "软院 22 数媒体 03 789"]
            }
        }
