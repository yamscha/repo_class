/*
import players.csv and seasons_stats.csv
If you need to edit the data type of the columns 6 and beyond,
mysql workbench only lets you edit the first 5 columns.
Use heidisql (windows) or sequelpro (mac) to import csv.
*/

SELECT players.*, seasons_stats.*
FROM players
INNER JOIN seasons_stats ON
players.player = seasons_stats.player
limit 50;

SELECT players.*, seasons_stats.*
FROM players
LEFT JOIN seasons_stats ON
players.player = seasons_stats.player
limit 50;

SELECT players.*, seasons_stats.*
FROM players
RIGHT JOIN seasons_stats ON
players.player = seasons_stats.player
limit 50;

/*
mysql does not have full outer joins.
use a union to create a full outer join
Note this takes a long time to run
*/
SELECT players.*, seasons_stats.*
FROM players
LEFT JOIN seasons_stats ON
players.player = seasons_stats.player
UNION
SELECT players.*, seasons_stats.*
FROM players
RIGHT JOIN seasons_stats ON
players.player = seasons_stats.player
limit 50;