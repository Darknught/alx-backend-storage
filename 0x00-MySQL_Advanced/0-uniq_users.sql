-- SQL script that creates a table users with attributes id, email, name
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY,
	email STRING VARCHAR(255) NOT NULL UNIQUE,
	name STRING VARCHAR(255)
);
