
-- import fcc complaints csv into new table

-- use 'alter table' to set primary key (it creates this query)
ALTER TABLE `Miscellaneous_DB`.`comcastfcccomplaints` 
CHANGE COLUMN `Ticket #` `Ticket #` INT(11) NOT NULL ,
ADD PRIMARY KEY (`Ticket #`);


select * from comcastfcccomplaints;

/*Use the gui to update or delete data.  Click 'apply' to make permanent*/