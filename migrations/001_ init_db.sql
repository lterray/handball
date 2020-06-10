CREATE TABLE player (
	id SERIAL PRIMARY KEY NOT NULL,
	first_name VARCHAR(125),
	last_name VARCHAR(125)
)

INSERT INTO player(first_name, last_name)
VALUES('laci', 'terray'), ('andrás', 'terray');