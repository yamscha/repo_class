USE animals_db;

DROP TABLE IF EXISTS people;

CREATE TABLE people (
  name VARCHAR(30) NOT NULL,
  has_pet BOOLEAN NOT NULL,
  pet_name VARCHAR(30),
  pet_age INTEGER(10),
  petting_cost_ratio DOUBLE(10,2),
  PRIMARY KEY (name)
);

SHOW TABLES;