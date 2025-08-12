from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class Score(BaseModel):
    job_id: int
    candidate_id: int
    resume_id: int
    total_score: float
    skills_score: Optional[float] = None
    experience_score: Optional[float] = None
    education_score: Optional[float] = None
    category_scores: Optional[Dict[str, float]] = None
    created_at: datetime = datetime.now()