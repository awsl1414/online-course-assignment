from sqlalchemy import Column, Integer, String
from core import Base


class Software(Base):
    __tablename__ = "软件表"
    id = Column(Integer, primary_key=True)
    classroomName = Column(String, nullable=False)
    software = Column(String, nullable=False)
