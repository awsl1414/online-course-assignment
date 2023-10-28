from sqlalchemy.orm import Session
from models import User


def create_user(db: Session, username: str, password: str, empno: str, role: str):
    user = User(username=username, hashed_password=password, empno=empno, role=role)
    db.add(user)
    db.commit()
    # db.refresh(user)
    return user
    # print(get_password_hash(password))
    # return "200"
