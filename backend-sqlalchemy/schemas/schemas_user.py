from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    job_number: str
    permission: int
    password: str


class UpdateUserIn(BaseModel):
    username: str
    reUsername: str | None = None
    rePassword: str | None = None
    reJob_number: str | None = None
    rePermission: int | None = None
