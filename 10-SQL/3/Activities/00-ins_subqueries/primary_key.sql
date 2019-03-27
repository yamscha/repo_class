/*
To ensure that a set of columns are unique as a group,
set multiple columns as the primary key.
*/
use Miscellaneous_db;
create table person(
	first_name varchar(50),
    last_name varchar(50),
    hobby varchar(50),
    primary key (first_name,last_name)
);

insert into person(first_name,last_name,hobby)
values("Tony","Li","skydiving");

insert into person(first_name,last_name,hobby)
values("Lena","Wang","base jumping");

insert into person(first_name,last_name,hobby)
values("Tony","Li","spelunking");
/*
Error Code: 1062. Duplicate entry 'Tony-Li' for key 'PRIMARY'
*/

insert into person(first_name,last_name,hobby)
values("Jet","Li","Wushu"); -- this is okay

insert into person(first_name,last_name,hobby)
values("Tony","Stark","Tinkering"); -- this is also okay

select * from person;
