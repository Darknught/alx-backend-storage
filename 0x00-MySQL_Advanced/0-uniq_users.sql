-- SQL script that creates a table users with attributes id, email, name
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	email STRING VARCHAR(255) UNIQUE NOT NULL,
	name STRING VARCHAR(255)
);
