SELECT s.store_id, SUM(amount) AS Gross
  FROM payment p
  JOIN rental r
  ON (p.rental_id = r.rental_id)
  JOIN inventory i
  ON (i.inventory_id = r.inventory_id)
  JOIN store s
  ON (s.store_id = i.store_id)
  GROUP BY s.store_id;

/*create a view as a shortcut for the subquery*/
CREATE VIEW total_sales AS
SELECT s.store_id, SUM(amount) AS Gross
FROM payment p
JOIN rental r
ON (p.rental_id = r.rental_id)
JOIN inventory i
ON (i.inventory_id = r.inventory_id)
JOIN store s
ON (s.store_id = i.store_id)
GROUP BY s.store_id;


select * from total_sales;

DROP VIEW total_sales;