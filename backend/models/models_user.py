from sqlalchemy import Column, Integer, String
from core import Base


class User(Base):
    __tablename__ = "UserTable"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    job_number = Column(String, nullable=False, comment="工号")
    hashed_password = Column(String, nullable=False)
    permission = Column(Integer, nullable=False, comment="权限")
