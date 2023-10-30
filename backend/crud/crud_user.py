from sqlalchemy.orm import Session
from models import User


def create_user(db: Session, username: str, password: str, job_number: str, permission: int):
    user = User(username=username, hashed_password=password, job_number=job_number,permission=permission)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    # print(get_password_hash(password))
    # return "200"
