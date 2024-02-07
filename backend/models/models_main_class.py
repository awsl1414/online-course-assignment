from sqlalchemy import Column, String, Integer
from utils import Base


class ModelsMainClass(Base):
    __tablename__ = "MainClassTable"
    id = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String, nullable=False, comment="教师姓名")
    teacher_room = Column(String, nullable=False, comment="教研室")
    course_name = Column(String, nullable=False, comment="课程名称")
    class_name = Column(String, nullable=False, comment="班级名称")
    population = Column(String, nullable=False, comment="人数")
    software_name = Column(String, nullable=False, comment="软件名称")
    computer_room_name = Column(String, nullable=False, comment="机房名称")
    day = Column(String, nullable=False)
    lesson = Column(String, nullable=False)
    cycle = Column(String, nullable=False, comment="周数")
