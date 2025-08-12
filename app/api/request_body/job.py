from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    title: str
    description: str
    required_skills: list[str]
    company: Optional[str] = None
    location: Optional[str] = None
    is_active: bool = True