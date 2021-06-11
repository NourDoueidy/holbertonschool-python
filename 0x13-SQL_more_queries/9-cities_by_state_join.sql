-- List all cities contained in hbtn_0d_usa
-- join and order by cities.id
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.states_id ORDER BY cities.id;
