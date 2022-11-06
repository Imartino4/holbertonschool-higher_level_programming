-- list all cities contained in hbtn_0d_usa
-- display: cities.id - cities.name - states.name
-- sorted in ascending order by cities.id
-- use only one SELECT
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id;