from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    firstname: str
    lastname: str
