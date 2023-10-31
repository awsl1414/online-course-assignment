from sqlalchemy import Column, Integer, String, Enum
from core import Base


class Origin(Base):
    __tablename__ = "OriginTable"
    id = Column(Integer, primary_key=True)
    teacherName = Column(String, nullable=False)
    courseName = Column(Enum("计算计网络", "无人机模拟"),nullable=False)
    population = Column(Integer, nullable=False)
    software = Column(String, nullable=False)
