from pydantic import BaseModel


class SchemasComputerRoomCreate(BaseModel):
    computer_room_name: str
    alias_name: str
    software_name: str
