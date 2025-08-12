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