USE animals_db;

drop table if exists people;
create table if not exists people(
  name varchar(50),
  has_pet boolean default false,
  pet_name varchar(50),
  pet_age integer(10),
  primary key(name)
);

INSERT INTO people (name, has_pet, pet_name, pet_age)
VALUES ("Victoria", true, "Blue", 10);

INSERT INTO people (name, has_pet, pet_name, pet_age)
VALUES ("Ken", true, "Rory", 4);

INSERT INTO people (name, has_pet, pet_name, pet_age)
VALUES ("Erica", true, "Oolong", 8);

INSERT INTO people (name, has_pet, pet_name, pet_age)
VALUES ("Nichole", true, "Rai", 3);

INSERT INTO people (name)
VALUES ("Steph");

SELECT * FROM people;

UPDATE people
SET has_pet = true, pet_name="Curry", pet_age=30
WHERE name = "Steph";

SELECT * FROM people;

