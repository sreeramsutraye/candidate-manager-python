from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str | None = None
    email: str
    password: str
    image_url: str | None = None
