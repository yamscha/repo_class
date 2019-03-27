-- Drops the programming_db if it already exists --
DROP DATABASE IF EXISTS programming_db;
-- Create a database called programming_db --
CREATE DATABASE IF NOT EXISTS programming_db;

USE programming_db;

CREATE TABLE programming_languages(
  -- Creates a numeric column called "id" which will automatically increment its default value as we create new rows. --
  id INTEGER(11) AUTO_INCREMENT NOT NULL,
  language VARCHAR(20),
  rating INTEGER(11),
  -- Creates a boolean column called "mastered" which will automatically fill --
  -- with true when a new row is made and the value isn't otherwise defined. --
  mastered BOOLEAN DEFAULT true,
  PRIMARY KEY (id)
);

-- Creates new rows
INSERT INTO programming_languages (language, rating)
VALUES ("Python", 95);

INSERT INTO programming_languages (language, rating)
VALUES ("VBA", 90);

INSERT INTO programming_languages (language, rating)
VALUES ("MySQL", 33);

INSERT INTO programming_languages (language, rating)
VALUES ("English", 100);

SELECT * FROM programming_languages;