
select * from film_actor limit 1;
select * from film limit 1;

SELECT *
FROM film f
INNER JOIN film_actor fa
ON (f.film_id = fa.film_id);

-- 
/* notice that 'DRUMELINE CYCLONE'
film_id of 257 does not exist in table film_actor.
Scroll to the rightmost columns and you'll see the 
columns are null for drumline cyclone
*/
SELECT *
FROM film f
LEFT OUTER JOIN film_actor fa
ON (f.film_id = fa.film_id)
where title like 'DRUM%';

SELECT *
FROM film f
LEFT OUTER JOIN film_actor fa
ON (f.film_id = fa.film_id)
WHERE fa.film_id IS NULL;