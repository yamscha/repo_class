

/* The % matches any number of characters*/
SELECT *
FROM actor
WHERE last_name LIKE 'Will%';

/* The _ matches a single character */
SELECT *
FROM actor
WHERE first_name LIKE '_AN';