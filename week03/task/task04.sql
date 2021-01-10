SELECT table01.id as 'table01.id', table01.name as 'table01.name', table02.id as 'table02.id', table02.name as 'table02.name'
FROM table01
RIGHT JOIN table02
ON table01.id = table02.id;
-- +------------+---------------+------------+---------------+
-- | table01.id | table01.name  | table02.id | table02.name  |
-- +------------+---------------+------------+---------------+
-- |          1 | table1_table2 |          1 | table1_table2 |
-- |       NULL | NULL          |          3 | table2        |
-- +------------+---------------+------------+---------------+

SELECT table01.id as 'table01.id', table01.name as 'table01.name', table02.id as 'table02.id', table02.name as 'table02.name'
FROM table01
LEFT JOIN table02
ON table01.id = table02.id;
-- +------------+---------------+------------+---------------+
-- | table01.id | table01.name  | table02.id | table02.name  |
-- +------------+---------------+------------+---------------+
-- |          1 | table1_table2 |          1 | table1_table2 |
-- |          2 | table1        |       NULL | NULL          |
-- +------------+---------------+------------+---------------+


SELECT table01.id as 'table01.id', table01.name as 'table01.name', table02.id as 'table02.id', table02.name as 'table02.name'
FROM table01
INNER JOIN table02
ON table01.id = table02.id;

-- +------------+---------------+------------+---------------+
-- | table01.id | table01.name  | table02.id | table02.name  |
-- +------------+---------------+------------+---------------+
-- |          1 | table1_table2 |          1 | table1_table2 |
-- +------------+---------------+------------+---------------+