from sqlalchemy import Column, Integer, String
from core import Base


class Floors(Base):
    __tablename__ = "FloorsTable"
    id = Column(Integer, primary_key=True)
    classRoomName = Column(String, nullable=False)
