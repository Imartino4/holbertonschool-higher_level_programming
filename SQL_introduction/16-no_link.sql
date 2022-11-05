-- list all records of second_table with name value
SELECT score, name FROM second_table WHERE name IS NOT null ORDER BY score DESC;