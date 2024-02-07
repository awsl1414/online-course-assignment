from sqlalchemy import Column, Integer, String
from utils import Base


class ModelsComputerRoom(Base):
    __tablename__ = "ComputerRoomTable"
    id = Column(Integer, primary_key=True, index=True)
    computer_room_name = Column(String, nullable=False, comment="机房名称")
    alias_name = Column(String, nullable=False, comment="机房别名")
    software_name = Column(String, nullable=False, comment="软件名称")
