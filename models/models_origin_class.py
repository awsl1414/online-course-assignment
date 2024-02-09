from sqlalchemy import Column, String, Integer
from utils import Base


class ModelsOriginClass(Base):
    __tablename__ = "OriginClassTable"
    id = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String, nullable=False, comment="教师姓名")
    course_name = Column(String, nullable=False, comment="课程名称")
    class_name = Column(String, nullable=False, comment="班级名称")
    population = Column(String, nullable=False, comment="人数")
    software_name = Column(String, nullable=False, comment="软件名称")
    cycle = Column(String, nullable=False, comment="周数")
    teacher_room = Column(String, nullable=False, comment="教研室")
    week_lesson_times = Column(Integer, nullable=False, comment="周课时")
