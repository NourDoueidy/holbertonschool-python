-- Create database hbtn_0d_usa
-- Create table cities
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS 'cities'@'hbtn_0d_usa' (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL FOREIGN KEY,
    name VARCHAR(256) NOT NULL
    REFERENCES 'hbtn_0d_usa'.'states'('id')
);
