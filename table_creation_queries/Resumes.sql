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

-- Insert dummy resumes (make sure user IDs match existing candidates)
INSERT INTO resumes (candidate_id, content, parsed_skills, file_url) VALUES
(1, 'JOHN SMITH
Senior Software Engineer with 8+ years of experience
john.smith@example.com | (555) 123-4567

SKILLS
- Programming Languages: Python, Java, JavaScript, Go
- Cloud Services: AWS (EC2, S3, Lambda), Google Cloud
- DevOps: Docker, Kubernetes, Jenkins, Terraform
- Databases: PostgreSQL, MongoDB, Redis
- Web Frameworks: Django, Spring Boot

EXPERIENCE
Senior Software Engineer | Tech Solutions Inc. | 2019-Present
- Led development of microservices architecture reducing system latency by 40%
- Implemented CI/CD pipelines using Jenkins and Docker
- Mentored junior developers and conducted code reviews

Software Engineer | CodeCorp | 2015-2019
- Developed RESTful APIs using Python and Django
- Optimized database queries improving performance by 35%
- Implemented automated testing increasing code coverage to 90%

EDUCATION
Master of Computer Science | Stanford University | 2015
Bachelor of Computer Science | University of California, Berkeley | 2013',
ARRAY['Python', 'Java', 'JavaScript', 'Go', 'AWS', 'Docker', 'Kubernetes', 'PostgreSQL', 'MongoDB', 'Django'],
'/uploads/resumes/john_smith_resume.pdf'),

(2, 'EMILY JOHNSON
Data Scientist
emily.johnson@example.com | (555) 234-5678

SKILLS
- Programming: Python, R, SQL
- Machine Learning: TensorFlow, PyTorch, scikit-learn
- Data Visualization: Tableau, Matplotlib, Seaborn
- Big Data: Spark, Hadoop
- Statistics: Hypothesis Testing, Regression Analysis

EXPERIENCE
Senior Data Scientist | DataInsights Corp. | 2020-Present
- Developed predictive models with 92% accuracy for customer churn
- Created automated data pipelines processing 50+ GB daily
- Led team of 3 data scientists on fraud detection project

Data Analyst | Analytics Co. | 2017-2020
- Performed exploratory data analysis on customer behavior
- Built dashboards using Tableau for executive reporting
- Improved marketing campaign effectiveness by 25%

EDUCATION
Ph.D. in Statistics | MIT | 2017
Bachelor of Science in Mathematics | Yale University | 2013',
ARRAY['Python', 'R', 'SQL', 'TensorFlow', 'PyTorch', 'scikit-learn', 'Tableau', 'Statistics'],
'/uploads/resumes/emily_johnson_resume.pdf'),

(3, 'MICHAEL WILLIAMS
Frontend Developer
michael.williams@example.com | (555) 345-6789

SKILLS
- Frontend: JavaScript, TypeScript, React, Vue.js, Angular
- Styling: CSS, SASS, Styled Components, Tailwind CSS
- Build Tools: Webpack, Babel, Vite
- Testing: Jest, React Testing Library
- Other: Git, npm, Agile

EXPERIENCE
Senior Frontend Developer | UIX Designs | 2021-Present
- Built responsive web applications using React and TypeScript
- Implemented state management with Redux and Context API
- Reduced bundle size by 35% improving load times significantly

Frontend Developer | WebCrafters | 2018-2021
- Developed interactive UI components with Vue.js
- Created mobile-first designs with CSS Grid and Flexbox
- Collaborated with designers to implement pixel-perfect interfaces

EDUCATION
Bachelor of Science in Computer Science | University of Washington | 2018',
ARRAY['JavaScript', 'TypeScript', 'React', 'Vue.js', 'CSS', 'SASS', 'Webpack', 'Jest', 'Git'],
'/uploads/resumes/michael_williams_resume.pdf'),

(4, 'SARAH BROWN
DevOps Engineer
sarah.brown@example.com | (555) 456-7890

SKILLS
- Cloud: AWS (EC2, S3, Lambda, ECS), Google Cloud Platform
- Containers: Docker, Kubernetes, ECS
- CI/CD: Jenkins, GitHub Actions, Travis CI
- Infrastructure as Code: Terraform, CloudFormation
- Monitoring: Prometheus, Grafana, ELK Stack
- Scripting: Bash, Python

EXPERIENCE
Lead DevOps Engineer | CloudSys Technologies | 2019-Present
- Implemented Kubernetes clusters reducing deployment time by 70%
- Automated infrastructure provisioning with Terraform
- Set up comprehensive monitoring and alerting system

Systems Administrator | TechOps Inc. | 2016-2019
- Managed Linux servers and network infrastructure
- Implemented backup and disaster recovery solutions
- Migrated on-premise applications to AWS cloud

EDUCATION
Master of Science in Computer Engineering | Georgia Tech | 2016
Bachelor of Science in IT | University of Texas | 2014',
ARRAY['AWS', 'Docker', 'Kubernetes', 'Jenkins', 'Terraform', 'Prometheus', 'Bash', 'Python'],
'/uploads/resumes/sarah_brown_resume.pdf'),

(5, 'DAVID JONES
Product Manager
david.jones@example.com | (555) 567-8901

SKILLS
- Product Management: Roadmapping, User Stories, PRDs
- Project Management: Agile, Scrum, Kanban, JIRA
- Analytics: Google Analytics, Mixpanel, A/B Testing
- Business: Market Analysis, Competitive Analysis, Revenue Models
- Communication: Stakeholder Management, Executive Presentations

EXPERIENCE
Senior Product Manager | ProductVision | 2020-Present
- Led development of mobile app increasing user engagement by 45%
- Defined product roadmap and quarterly OKRs
- Coordinated cross-functional teams (engineering, design, marketing)

Product Manager | TechStartup | 2017-2020
- Launched 3 successful product features generating $1.2M in revenue
- Conducted user research and usability testing
- Prioritized backlog based on business impact and technical constraints

EDUCATION
MBA | Harvard Business School | 2017
Bachelor of Business Administration | NYU | 2014',
ARRAY['Agile', 'Scrum', 'JIRA', 'Product Strategy', 'User Research', 'Google Analytics', 'Roadmapping'],
'/uploads/resumes/david_jones_resume.pdf');