-- create db hbtn_0d_usa and table citues:
-- cities: id int unique autogen, not null primary key
-- cities: state_id unt not null foreign key that reference id of states
-- cities: name varchar(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id int AUTO_INCREMENT,
    state_id int NOT NULL,
    name varchar(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);