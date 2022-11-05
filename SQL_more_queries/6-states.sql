-- creates db hbtn_0d_usa and table states
-- states: id INT unique, auto generated can't be null and is a primary key
-- states: name varchar(256) not null
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS 'states' (
    id int UNIQUE AUTO_INCREMENT PRIMARY KEY,
    name varchar(256) NOT NULL
);