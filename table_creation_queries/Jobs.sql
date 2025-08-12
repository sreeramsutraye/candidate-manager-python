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

-- Insert dummy jobs
INSERT INTO jobs (title, description, required_skills, company, location, is_active) VALUES
('Senior Software Engineer', 'We are looking for a Senior Software Engineer with strong experience in backend development. The ideal candidate should have expertise in building scalable applications and leading development teams. Responsibilities include designing system architecture, writing clean code, mentoring junior developers, and participating in code reviews.', 
ARRAY['Python', 'Java', 'AWS', 'Microservices', 'Docker', 'Kubernetes', 'SQL'], 
'Tech Innovations Inc.', 'San Francisco, CA', TRUE),

('Data Scientist', 'Join our data science team to work on challenging problems using machine learning and statistical analysis. You will be responsible for developing predictive models, analyzing large datasets, and deriving actionable insights to drive business decisions.',
ARRAY['Python', 'R', 'SQL', 'Machine Learning', 'TensorFlow', 'PyTorch', 'Statistics'], 
'DataCorp Analytics', 'Boston, MA', TRUE),

('Frontend Developer', 'We are seeking a talented Frontend Developer to create responsive and intuitive user interfaces. The ideal candidate will have strong experience with modern JavaScript frameworks and a keen eye for design.',
ARRAY['JavaScript', 'React', 'HTML', 'CSS', 'TypeScript', 'Redux', 'Webpack'], 
'WebUI Solutions', 'Austin, TX', TRUE),

('DevOps Engineer', 'Looking for a DevOps Engineer to streamline our deployment processes and maintain our cloud infrastructure. The ideal candidate will have experience with CI/CD pipelines and cloud services.',
ARRAY['AWS', 'Docker', 'Kubernetes', 'Jenkins', 'Terraform', 'Linux', 'Bash'], 
'CloudOps Technologies', 'Seattle, WA', TRUE),

('Product Manager', 'We need an experienced Product Manager to lead our product development efforts. You will work closely with engineering, design, and marketing teams to define product strategy and roadmap.',
ARRAY['Agile', 'JIRA', 'Product Strategy', 'User Research', 'Roadmapping', 'Analytics'], 
'ProductFirst Inc.', 'New York, NY', TRUE);