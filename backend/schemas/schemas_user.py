from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    job_number: str
    permission: int
    password: str
