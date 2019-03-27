CREATE DATABASE people_db;
USE people_db;

create table students(
id integer(10) auto_increment not null,
name varchar(50) not null,
city varchar(50),
food varchar(50),
hours_sleep_per_week integer(10),
hours_studying_per_week integer(10),
alcohol_servings_per_week integer(10),
shopping_expense_per_month double(10,2),
primary key (id)
);

insert into students(name,city,food,hours_sleep_per_week,hours_studying_per_week,alcohol_servings_per_week,shopping_expense_per_month)
values ('eddy','montreal','xiaolongboa',70,20,7,10.50);

select * from students;
-- drop table people;
