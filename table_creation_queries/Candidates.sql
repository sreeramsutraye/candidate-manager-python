-- Create a custom type for the candidate status for better data integrity.
CREATE TYPE candidate_status AS ENUM ('Created', 'Contacted', 'Interviewing', 'Offered', 'Hired', 'Rejected');

-- Main table to store candidate information
CREATE TABLE candidate (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255),
    title VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50) UNIQUE NOT NULL,
    github VARCHAR(255),
    linkedin VARCHAR(255),
    resume BYTEA,
    status candidate_status DEFAULT 'Created',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store candidate's educational background
-- A candidate can have multiple education entries.
CREATE TABLE education (
    id SERIAL PRIMARY KEY,
    candidate_id INT REFERENCES candidate(id) ON DELETE CASCADE,
    school VARCHAR(255) NOT NULL,
    from_year INT NOT NULL,
    to_year INT NOT NULL,
    course VARCHAR(255) NOT NULL,
    description TEXT
);

-- Table to store candidate's work experience
-- A candidate can have multiple experience entries.
CREATE TABLE experience (
    id SERIAL PRIMARY KEY,
    candidate_id INT REFERENCES candidate(id) ON DELETE CASCADE,
    company_name VARCHAR(255) NOT NULL,
    from_year INT NOT NULL,
    from_month INT NOT NULL,
    to_year INT NOT NULL,
    to_month INT NOT NULL, -- Corrected from the model which had two to_year fields
    description TEXT
);

-- Table to store candidate's achievements
-- This one-to-many relationship is better than an array in the main table.
CREATE TABLE achievement (
    id SERIAL PRIMARY KEY,
    candidate_id INT REFERENCES candidate(id) ON DELETE CASCADE,
    achievement_description TEXT NOT NULL
);

-- Automatically update the updated_at timestamp on any change to the candidate record
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$ language 'plpgsql';


CREATE TRIGGER update_candidate_updated_at
BEFORE UPDATE ON candidate
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

ALTER TABLE candidate
ADD is_deleted BOOLEAN DEFAULT FALSE;









