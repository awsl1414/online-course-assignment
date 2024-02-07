from sqlalchemy import Column, String, Integer
from utils import Base


class ModelsMainClass(Base):
    __tablename__ = "MainClassTable"
    id = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String, nullable=False)
    teacher_room = Column(String, nullable=False)
    course_name = Column(String, nullable=False)
    class_name = Column(String, nullable=False)
    population = Column(String, nullable=False)
    software_name = Column(String, nullable=False)
    computer_room_name = Column(String, nullable=False)
    day = Column(String, nullable=False)
    lesson = Column(String, nullable=False)
    cycle = Column(String, nullable=False)  # 周期
