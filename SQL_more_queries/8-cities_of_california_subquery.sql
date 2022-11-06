-- list all the cities of California that can be founded in hbtn_0d_usa
-- states: (id, name) = 1 2 3 4, California, Arizona, Texas, Utah)
-- cities: (id, state_id, name) = (1 2 4 6 7 8, 1 1 2 3 3, SanFrancisco SanJose Page Paris Houston)
-- id of states could be different (California is not always 1)
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');