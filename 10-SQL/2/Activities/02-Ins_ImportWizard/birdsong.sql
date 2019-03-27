
create database if not exists Miscellaneous_DB;
use Miscellaneous_DB;

-- use import wizard, import birdsong.csv
select * from birdsong limit 10;
select count(*) from birdsong;

-- after it creates the table, import more data from birdsong_data.csv
select count(*) from birdsong;

SELECT * FROM birdsong WHERE genus = "Acanthis";

SELECT * FROM birdsong 
WHERE genus = "Acanthis" 
AND country = "Netherlands";


SELECT * FROM birdsong
WHERE GENUS not in ('Acanthis', 'Acrocephalus');

SELECT * FROM birdsong
WHERE GENUS != 'Acanthis';

SELECT * FROM birdsong
WHERE NOT (genus = "Acanthis" AND country = "Netherlands");
