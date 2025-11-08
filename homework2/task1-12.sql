--1
SELECT
    d.id AS department_id,
    COUNT(*) AS employee_count
FROM
    departments AS d
    JOIN employees AS e ON d.id = = e.department_id
GROUP BY
    department_id
HAVING
    employee_count < 10;

--2
SELECT
    e.name,
    e.salary,
    p.salary
FROM
    employees e
    JOIN employees p ON e.chief_id = p.id
WHERE
    e.salary > p.salary;

--3
SELECT
    e.id,
    e.name
FROM
    employees e
    JOIN employees p ON e.chief_id = p.id
WHERE
    e.department_id != p.department_id;

--4
SELECT
    SUM(items * price) AS income_from_female
FROM
    purchases;

--5
SELECT
    p.owner_id,
    COUNT(*) AS post_count
FROM
    profile AS pf
    JOIN post AS p ON pf.id = p.owner_id
GROUP BY
    p.owner_id
HAVING
    post_count > 10;

--6
SELECT
    company,
    COUNT(*) AS product_count
FROM
    products
WHERE
    price > 30000
GROUP BY
    company
HAVING
    COUNT(*) > 0;

--7
SELECT
    a.author_id,
    a.author_name,
    SUM(b.book_sold) AS total_books_sold
FROM
    authors AS a
    JOIN books_authors ba ON a.author_id = ba.author_id
    JOIN books b ON ba.book_id = b.book_id
GROUP BY
    a.author_id,
    a.author_name
LIMIT
    5;

--8
SELECT
    countries.name,
    COUNT(*)
FROM
    country_languages
    JOIN countries ON country_languages.country_code = countries.code
GROUP BY
    country_languages.country_code
ORDER BY
    country_languages.country_code desc
LIMIT
    1;

--9
SELECT
    name,
    population AS total_population
FROM
    countries
ORDER BY
    total_population desc
LIMIT
    1;

--10
SELECT
    pf.nickname,
    COUNT(*) AS post_count
FROM
    profile AS pf
    JOIN post AS p ON pf.id = p.owner_id
GROUP BY
    pf.nickname
HAVING
    post_count < 3;

--11
SELECT
    b.book_name,
    COUNT(ba.author_id) AS authors_count
FROM
    books_authors AS ba
    JOIN books AS b ON b.book_id = ba.book_id
GROUP BY
    b.book_id
HAVING
    COUNT(ba.author_id) > 1;

--12
SELECT
    language,
    COUNT(is_official) AS countries_count
FROM
    country_languages
WHERE
    is_official = 'T'
GROUP BY
    language
HAVING
    COUNT(is_official) > 1;
