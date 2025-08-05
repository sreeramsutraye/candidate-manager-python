from pydantic import BaseModel

class Education(BaseModel):
    school: str
    from_year: int
    to_year: int
    course: str
    description: str | None = None

class Experience(BaseModel):
    company_name: str
    from_year: int
    from_month: int
    to_year: int
    to_year: int
    description: str | None = None

class Candidate(BaseModel):
    first_name: str
    last_name: str | None = None
    email : str
    phone: str
    achievement: list[str]
    education: list[Education]
    experience: list[Experience]
    github: str | None = None
    linkedin: str | None = None
    resume: bytes | None = None
    status: str | None = "Created"
