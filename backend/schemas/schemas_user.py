from pydantic import BaseModel

class User(BaseModel):
    username:str
    job_number:str
    permission:int
class UserIn(User):
    password: str

