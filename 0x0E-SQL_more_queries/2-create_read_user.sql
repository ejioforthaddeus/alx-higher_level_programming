-- Create databasee and new user and grant SELECT permision to the user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant user permision
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
