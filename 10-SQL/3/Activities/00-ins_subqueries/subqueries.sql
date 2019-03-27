use sakila;
show tables;

SELECT *
FROM film
WHERE title = 'Velvet Terminator';


SELECT film_id
FROM film
WHERE title = 'Velvet Terminator';

SELECT *
FROM inventory
WHERE film_id = 938;

/*join*/
SELECT i.*
FROM inventory i
JOIN film f
ON (i.film_id = f.film_id)
WHERE f.title = 'Velvet Terminator';

/*subquery*/
select * from inventory where film_id in (
  select film_id from film where title = 'Velvet Terminator'
);

/*
Which is more efficient?
https://stackoverflow.com/questions/2577174/join-vs-sub-query
*/