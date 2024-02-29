from pydantic import BaseModel


class BaseOriginClass(BaseModel):
    teacher_name: str
    course_name: str
    class_name: str
    population: int
    software_name: str
    cycle: str
    teacher_room: str
    week_lesson_times: int
    is_ok: int

    class Config:
        from_attributes = True


class SchemasOriginClassCreate(BaseOriginClass):
    pass


class SchemasOriginClassUpdate(BaseOriginClass):
    id: int
