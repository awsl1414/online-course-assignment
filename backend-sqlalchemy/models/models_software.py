from sqlalchemy import Column, Integer, String
from core import Base


class Software(Base):
    __tablename__ = "SoftwareTable"
    id = Column(Integer, primary_key=True)
    classRoomName = Column(String, nullable=False)
    software = Column(String, nullable=False)
