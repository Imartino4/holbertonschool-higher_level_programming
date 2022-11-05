-- create table id_not_null with id and name:
-- id int with default value 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id int DEFAULT 1,
    name varchar(256)
);