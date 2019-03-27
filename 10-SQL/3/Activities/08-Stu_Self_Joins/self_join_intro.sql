
SELECT A.NAME, B.NAME, A.CITY
FROM customer_list A
JOIN customer_list B
USING (city)
WHERE A.ID <> B.ID;