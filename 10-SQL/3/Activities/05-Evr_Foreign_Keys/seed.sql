CREATE TABLE animals_all (
 id INTEGER(11) AUTO_INCREMENT NOT NULL,
 animal_species VARCHAR(30) NOT NULL,
 owner_name VARCHAR(30) NOT NULL,
 PRIMARY KEY (id)
);

INSERT INTO animals_all (animal_species, owner_name) 
VALUES 
("Dog", "Bob"),
("Fish", "Bob"),
("Cat", "Kelly"),
("Dolphin", "Aquaman");


CREATE TABLE animals_location (
 id INTEGER(11) AUTO_INCREMENT NOT NULL,
 location VARCHAR(30) NOT NULL,
 animal_id INTEGER(10) NOT NULL,
 PRIMARY KEY (id),
 FOREIGN KEY (animal_id) REFERENCES animals_all(id) 
);

INSERT INTO animals_location (location, animal_id) VALUES ("Doghouse", 1);
INSERT INTO animals_location (location, animal_id) VALUES ("Fish tank", 2);
INSERT INTO animals_location (location, animal_id) VALUES ("Bed", 3);
INSERT INTO animals_location (location, animal_id) VALUES ("Ocean", 4);

SELECT * FROM animals_location;

/* this will give an error, 
because the id 5 doesn't exist in the animals_all table*/
INSERT INTO animals_location (location, animal_id)
VALUES ("River", 5);

/*this is okay, because id 4 exists in animals_all*/
INSERT INTO animals_location (location, animal_id)
VALUES ("River", 4);

SELECT * FROM animals_location; 