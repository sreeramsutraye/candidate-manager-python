from fastapi import APIRouter, HTTPException
from api.request_body.score import Score
from api.db.db_manager import execute_query
from api.scoring.scorer import Scorer
from typing import List, Dict

router = APIRouter()
scorer = Scorer()

@router.post("/score")
async def calculate_score(job_id: int, resume_id: int):
    # Get job and resume details
    job_query = "SELECT * FROM jobs WHERE id = $1;"
    job_params = (job_id,)
    job_result = await execute_query(job_query, job_params)
    
    if not job_result:
        raise HTTPException(status_code=404, detail="Job not found")
    
    resume_query = "SELECT * FROM resumes WHERE id = $1;"
    resume_params = (resume_id,)
    resume_result = await execute_query(resume_query, resume_params)
    
    if not resume_result:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    job = job_result[0]
    resume = resume_result[0]
    
    # Calculate the score
    score = scorer.calculate_score(job["description"], resume["content"])
    
    # Store the score in the database
    store_query = """
        INSERT INTO scores (job_id, candidate_id, resume_id, total_score)
        VALUES ($1, $2, $3, $4)
        RETURNING id
    """
    store_params = (job_id, resume["candidate_id"], resume_id, score)
    result = await execute_query(store_query, store_params)
    score_id = result[0]["id"] if result else None
    
    return {
        "score_id": score_id,
        "job_id": job_id,
        "resume_id": resume_id,
        "candidate_id": resume["candidate_id"],
        "score": score
    }

@router.get("/scores/job/{job_id}")
async def get_job_scores(job_id: int):
    query = """
        SELECT s.*, c.first_name, c.last_name, c.email
        FROM scores s
        JOIN users c ON s.candidate_id = c.id
        WHERE s.job_id = $1
        ORDER BY s.total_score DESC;
    """
    params = (job_id,)
    result = await execute_query(query, params)
    return result

@router.get("/scores/candidate/{candidate_id}")
async def get_candidate_scores(candidate_id: int):
    query = """
        SELECT s.*, j.title as job_title, j.company
        FROM scores s
        JOIN jobs j ON s.job_id = j.id
        WHERE s.candidate_id = $1
        ORDER BY s.created_at DESC;
    """
    params = (candidate_id,)
    result = await execute_query(query, params)
    return result