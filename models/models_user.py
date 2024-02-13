from sqlalchemy import Column, Integer, String
from utils import Base
from utils.security import get_password_hash


class ModelsUser(Base):
    __tablename__ = "UserTable"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True, comment="用户名")
    job_number = Column(String, nullable=False, unique=True, comment="工号")
    _hashed_password = Column(String, nullable=False, unique=True, comment="密码")
    permission = Column(Integer, nullable=False, comment="权限")

    @property
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, password: str):
        self._hashed_password = get_password_hash(password)
