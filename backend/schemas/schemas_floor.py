from pydantic import BaseModel


class SchemasUserCreate(BaseModel):
    username: str
    hashed_password: str
    job_number: str
    permission: int
