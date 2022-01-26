DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  artist_id INT REFERENCES artists(id),
  genre VARCHAR(255)
  
);

-- INSERT INTO albums (name) 
-- VALUES ('name1');

-- INSERT INTO albums (name) 
-- VALUES ('name2');

-- INSERT INTO albums (name) 
-- VALUES ('name3');

-- INSERT INTO albums (name) 
-- VALUES ('name4');

-- INSERT INTO albums (name) 
-- VALUES ('name5');

-- INSERT INTO albums ( name, genre) 
-- VALUES ('album1', 'rock');

-- INSERT INTO albums ( name, genre) 
-- VALUES ('album2', 'punk');

-- INSERT INTO albums ( name, genre) 
-- VALUES ('album3', 'pop');

-- INSERT INTO albums ( name, genre) 
-- VALUES ('album4', 'jazz');

-- INSERT INTO albums ( name, genre) 
-- VALUES ('album5', 'classical');