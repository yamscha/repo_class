/*
import globalfirepower.csv
Note that you can wrap column names around quotes to handle spaces:
select 'Total Aircraft Strength' from globalfirepower limit 5;

Also, you can use mysqlworkbench to alter table column names.
Right-click the table and click 'alter table'.
*/

-- altering original table:
use Miscellaneous_DB;

ALTER TABLE `Miscellaneous_DB`.`globalfirepower` 
CHANGE COLUMN `Total Population` `TotalPopulation` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Manpower Available` `ManpowerAvailable` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Fit-for-Service` `FitForService` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Reaching Military Age` `ReachingMilitaryAge` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Total Military Personnel` `TotalMilitaryPersonnel` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Active Personnel` `ActivePersonnel` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Reserve Personnel` `ReservePersonnel` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Total Aircraft Strength` `TotalAircraftStrength` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Fighter Aircraft` `FighterAircraft` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Attack Aircraft` `AttackAircraft` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Transport Aircraft` `TransportAircraft` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Trainer Aircraft` `TrainerAircraft` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Total Helicopter Strength` `TotalHelicopterStrength` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Attack Helicopters` `AttackHelicopters` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Combat Tanks` `CombatTanks` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Armored Fighting Vehicles` `ArmoredFightingVehicles` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Self-Propelled Artillery` `SelfPropelledArtillery` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Towed Artillery` `TowedArtillery` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Rocket Projectors` `RocketProjectors` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Total Naval Assets` `TotalNavalAssets` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Aircraft Carriers` `AircraftCarriers` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Patrol Craft` `PatrolCraft` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Mine Warfare Vessels` `MineWarfareVessels` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Production (bbl/dy)` `Production_bbl_dy` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Consumption (bbl/dy)` `Consumption_bbl_dy` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Proven Reserves (bbl)` `ProvenReserves_bbl` BIGINT(20) NULL DEFAULT NULL ,
CHANGE COLUMN `Labor Force` `LaborForce` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Merchant Marine Strength` `MerchantMarineStrength` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Major Ports / Terminals` `MajorPorts_per_Terminals` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Roadway Coverage (km)` `RoadwayCoverage_km` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Railway Coverage (km)` `RailwayCoverage_km` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Serivecable Airports` `SerivecableAirports` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Defense Budget` `DefenseBudget` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `External Debt` `ExternalDebt` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Foreign Exchange / Gold` `ForeignExchange_per_Gold` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Purchasing Power Parity` `PurchasingPowerParity` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Square Land Area (km)` `SquareLandArea_km` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Coastline (km)` `Coastline_km` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Shared Borders (km)` `SharedBorders_km` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `Waterways (km)` `Waterways_km` INT(11) NULL DEFAULT NULL ;


select count(*) from globalfirepower; -- 80

select count(*) from globalfirepower
where ReservePersonnel = 0; -- 8
/*
Error Code: 1175. You are using safe update mode and 
you tried to update a table without a WHERE that uses a KEY column 
To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.
Note: uncheck safe updates. Then exit and reconnect to mysql server.

*/

DELETE FROM globalfirepower
WHERE ReservePersonnel = 0; -- delete 8

select count(*) from globalfirepower; -- 72

select * from globalfirepower
where FighterAircraft = 0;

UPDATE globalfirepower
SET FighterAircraft = 1, TotalAircraftStrength = TotalAircraftStrength + 1
WHERE FighterAircraft = 0;

select * from globalfirepower
where FighterAircraft = 1;

SELECT AVG(TotalMilitaryPersonnel), -- 741101
AVG(TotalAircraftStrength), -- 639
AVG(TotalHelicopterStrength), -- 257
AVG(TotalPopulation) -- 85175106
FROM globalfirepower; 


INSERT INTO globalfirepower(Country, 
TotalPopulation, 
TotalMilitaryPersonnel, 
TotalAircraftStrength, 
TotalHelicopterStrength)
select 'Wakanda', 
AVG(TotalPopulation),
AVG(TotalMilitaryPersonnel),
AVG(TotalAircraftStrength),
AVG(TotalHelicopterStrength)
from globalfirepower
where Country != 'Wakanda';

select * from globalfirepower where Country = 'Wakanda';