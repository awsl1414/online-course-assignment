from sqlalchemy import Column, Integer, String
from utils import Base


class ModelsUser(Base):
    __tablename__ = "UserTable"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True, comment="用户名")
    job_number = Column(String, nullable=False, unique=True, comment="工号")
    hashed_password = Column(String, nullable=False, unique=True, comment="密码")
    permission = Column(Integer, nullable=False, comment="权限")
