/*
create miscellaneous_db if it doesn't already exist
first import wordassociation-ac.csv and create a new table
then import wordassociation-bc.csv into the same table
then import wordassociation-cc.csv
Explore the resulting table
*/
create database if not exists Miscellaneous_DB;
use Miscellaneous_DB;

SELECT * FROM wordassociation
WHERE source = "AC";

SELECT * FROM wordassociation
WHERE author >= 0 AND author <= 20;

SELECT * FROM wordassociation
WHERE word1 = "pie" OR word2 = "pie";

select * from wordassociation limit 5;
select max(author) from wordassociation; -- 759

select count(*) from wordassociation; -- 48964

select min(author) from wordassociation where source='CC'; -- 723

select count(*) from wordassociation where author=12; -- 4040