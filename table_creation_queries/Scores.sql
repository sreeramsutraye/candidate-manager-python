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
