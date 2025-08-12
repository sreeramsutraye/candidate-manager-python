from fastapi import APIRouter, HTTPException
from api.request_body.job import Job
from api.db.db_manager import execute_query
from typing import List, Dict, Any

router = APIRouter()

@router.post("/jobs")
async def create_job(job: Job):
    query = """
        INSERT INTO jobs (title, description, required_skills, company, location, is_active)
        VALUES ($1, $2, $3, $4, $5, $6)
        RETURNING id
    """
    params = (job.title, job.description, job.required_skills, job.company, job.location, job.is_active)
    result = await execute_query(query, params)
    job_id = result[0]["id"] if result else None
    return {"job_id": job_id, "message": "Job created successfully"}

@router.get("/jobs")
async def get_jobs():
    query = "SELECT * FROM jobs WHERE is_active = TRUE;"
    jobs = await execute_query(query)
    return jobs

@router.get("/jobs/{job_id}")
async def get_job(job_id: int):
    query = "SELECT * FROM jobs WHERE id = $1;"
    params = (job_id,)
    result = await execute_query(query, params)
    if not result:
        raise HTTPException(status_code=404, detail="Job not found")
    return result[0]

@router.put("/jobs/{job_id}")
async def update_job(job_id: int, job: Job):
    query = """
        UPDATE jobs
        SET title = $1, description = $2, required_skills = $3, company = $4, location = $5, is_active = $6
        WHERE id = $7
    """
    params = (job.title, job.description, job.required_skills, job.company, job.location, job.is_active, job_id)
    await execute_query(query, params)
    return {"message": "Job updated successfully"}

@router.delete("/jobs/{job_id}")
async def delete_job(job_id: int):
    query = """
        UPDATE jobs
        SET is_active = FALSE
        WHERE id = $1
    """
    params = (job_id,)
    await execute_query(query, params)
    return {"message": "Job deleted successfully"}