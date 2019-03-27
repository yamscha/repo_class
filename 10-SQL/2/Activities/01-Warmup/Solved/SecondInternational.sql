/*
decimal, numeric: https://dev.mysql.com/doc/refman/5.7/en/fixed-point-types.html
double, float: https://dev.mysql.com/doc/refman/5.7/en/floating-point-types.html
Just use decimal
*/

drop database if exists Second_International_Bank;
create database Second_International_Bank;
use Second_International_Bank;

create table Customers (
	ID int(50) auto_increment,
    FirstName varchar(50),
    LastName varchar(50),
    Loan decimal(20,2),
    Checking decimal(20,2),
    Savings decimal(20,2),
    primary key(ID)
);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Heidi", "Lendenberger", 2000.00, 1000.00, 20000.50);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Charles", "Pontier", 50000.00, 10.75, 2.05);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Dolly", "Ye", 0.00, 1000000.00, 50000025.00);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Adam", "Mercier", 100.00, 250.00, 10000.00);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Brian", "Diemer", 2000.00, 1000.00, 20000.50);

select * from Customers;