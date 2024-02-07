from pydantic import BaseModel


class BaseMainClass(BaseModel):
    teacher_name: str
    course_name: str
    class_name: str
    population: int
    software_name: str
    computer_room_name: str
    day: str
    lesson: str
    cycle: str
    teacher_room: str

    class Config:
        from_attributes = True


class SchemasMainClassCreate(BaseMainClass):
    pass


class SchemasMainClassUpdate(BaseMainClass):
    id: int


class BaseOriginClass(BaseModel):
    teacher_name: str
    course_name: str
    class_name: str
    population: int
    software_name: str
    cycle: str
    teacher_room: str
    week_lesson_times: int

    class Config:
        from_attributes = True


class SchemasOriginClassCreate(BaseOriginClass):
    pass


class SchemasOriginClassUpdate(BaseOriginClass):
    id: int
