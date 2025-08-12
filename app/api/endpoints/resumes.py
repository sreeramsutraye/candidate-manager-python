from fastapi import APIRouter, HTTPException, UploadFile, File
from api.request_body.resume import Resume
from api.db.db_manager import execute_query
from typing import List
import uuid
import os

router = APIRouter()

@router.post("/resumes")
async def upload_resume(candidate_id: int, resume_file: UploadFile = File(...)):
    # Save the resume file
    file_extension = os.path.splitext(resume_file.filename)[1]
    file_name = f"{uuid.uuid4()}{file_extension}"
    file_path = f"uploads/resumes/{file_name}"
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "wb") as f:
        content = await resume_file.read()
        f.write(content)
    
    # For now, just store the raw text content
    resume_content = content.decode("utf-8", errors="ignore")
    
    # Create a resume entry in the database
    query = """
        INSERT INTO resumes (candidate_id, content, file_url)
        VALUES ($1, $2, $3)
        RETURNING id
    """
    params = (candidate_id, resume_content, file_path)
    result = await execute_query(query, params)
    resume_id = result[0]["id"] if result else None
    
    return {"resume_id": resume_id, "message": "Resume uploaded successfully"}

@router.get("/resumes/{resume_id}")
async def get_resume(resume_id: int):
    query = "SELECT * FROM resumes WHERE id = $1;"
    params = (resume_id,)
    result = await execute_query(query, params)
    if not result:
        raise HTTPException(status_code=404, detail="Resume not found")
    return result[0]

@router.get("/candidates/{candidate_id}/resumes")
async def get_candidate_resumes(candidate_id: int):
    query = "SELECT * FROM resumes WHERE candidate_id = $1;"
    params = (candidate_id,)
    result = await execute_query(query, params)
    return result