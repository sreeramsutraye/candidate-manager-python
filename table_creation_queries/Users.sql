CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    image_url VARCHAR(255)
);

SELECT * from users;

ALTER TABLE users
ADD is_deleted BOOLEAN DEFAULT FALSE;


-- Insert dummy candidates into users table
INSERT INTO users (id,first_name, last_name, email, password, is_deleted) VALUES
(2,'John', 'Smith', 'john.smith@example.com', 'password123', FALSE),
(3,'Emily', 'Johnson', 'emily.johnson@example.com', 'password123', FALSE),
(4,'Michael', 'Williams', 'michael.williams@example.com', 'password123', FALSE),
(5,'Sarah', 'Brown', 'sarah.brown@example.com', 'password123', FALSE),
(6,'David', 'Jones', 'david.jones@example.com', 'password123', FALSE),
(7,'Jennifer', 'Miller', 'jennifer.miller@example.com', 'password123', FALSE),
(8,'Robert', 'Davis', 'robert.davis@example.com', 'password123', FALSE),
(9,'Jessica', 'Garcia', 'jessica.garcia@example.com', 'password123', FALSE),
(10,'Thomas', 'Rodriguez', 'thomas.rodriguez@example.com', 'password123', FALSE),
(11,'Lisa', 'Wilson', 'lisa.wilson@example.com', 'password123', FALSE);
