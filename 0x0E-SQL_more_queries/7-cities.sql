-- creates a new database with new table in it, with refernced to state table.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT, name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id));
