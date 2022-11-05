-- create table unique_id:
-- id with default value=1 and unique
CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 UNIQUE,
    name varchar(256)
);