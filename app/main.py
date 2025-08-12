from fastapi import FastAPI
from api.endpoints import users, jobs, resumes, scores
import uvicorn

app = FastAPI(title="Candidate Manager API", version="1.0.0")

# Include routers
app.include_router(users.app, tags=["Users"])
app.include_router(jobs.router, prefix="/api", tags=["Jobs"])
app.include_router(resumes.router, prefix="/api", tags=["Resumes"])
app.include_router(scores.router, prefix="/api", tags=["Scores"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Candidate Manager API"}

# SQLAlchemy models would be defined in a separate file, typically in a 'models' directory.
# Here we just define the tables as comments for reference.

"""
-- Add these tables to your database schema

-- Jobs table
CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    required_skills TEXT[] NOT NULL,
    company VARCHAR(255),
    location VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Resumes table
CREATE TABLE IF NOT EXISTS resumes (
    id SERIAL PRIMARY KEY,
    candidate_id INTEGER REFERENCES users(id),
    content TEXT NOT NULL,
    parsed_skills TEXT[],
    education TEXT[],
    experience TEXT[],
    file_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scores table
CREATE TABLE IF NOT EXISTS scores (
    id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES jobs(id),
    candidate_id INTEGER REFERENCES users(id),
    resume_id INTEGER REFERENCES resumes(id),
    total_score FLOAT NOT NULL,
    skills_score FLOAT,
    experience_score FLOAT,
    education_score FLOAT,
    category_scores JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
