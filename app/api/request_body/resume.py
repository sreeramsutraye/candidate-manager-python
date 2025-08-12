from pydantic import BaseModel
from typing import Optional

class Resume(BaseModel):
    candidate_id: int
    content: str
    parsed_skills: Optional[list[str]] = None
    education: Optional[list[str]] = None
    experience: Optional[list[str]] = None
    file_url: Optional[str] = None