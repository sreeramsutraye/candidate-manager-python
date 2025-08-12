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

-- Insert dummy scores (matching jobs with candidates)
INSERT INTO scores (job_id, candidate_id, resume_id, total_score, skills_score, experience_score, education_score) VALUES
(1, 1, 1, 85.7, 90.2, 82.5, 78.0),  -- John Smith (Software Engineer) for Senior Software Engineer position
(2, 2, 2, 92.3, 95.0, 88.5, 96.0),  -- Emily Johnson (Data Scientist) for Data Scientist position
(3, 3, 3, 88.5, 92.0, 85.0, 75.0),  -- Michael Williams (Frontend Developer) for Frontend Developer position
(4, 4, 4, 90.1, 94.5, 87.2, 82.0),  -- Sarah Brown (DevOps Engineer) for DevOps Engineer position
(5, 5, 5, 82.6, 85.0, 80.0, 78.0),  -- David Jones (Product Manager) for Product Manager position
(1, 2, 2, 45.2, 30.0, 55.0, 65.0),  -- Emily Johnson (Data Scientist) for Software Engineer position (low match)
(2, 1, 1, 50.5, 42.0, 60.0, 45.0),  -- John Smith (Software Engineer) for Data Scientist position (medium match)
(3, 5, 5, 30.8, 25.0, 40.0, 35.0),  -- David Jones (Product Manager) for Frontend Developer position (low match)
(4, 3, 3, 42.3, 38.0, 45.0, 50.0),  -- Michael Williams (Frontend) for DevOps position (low match)
(5, 4, 4, 55.7, 50.0, 62.0, 48.0);  -- Sarah Brown (DevOps) for Product Manager position (medium match)
