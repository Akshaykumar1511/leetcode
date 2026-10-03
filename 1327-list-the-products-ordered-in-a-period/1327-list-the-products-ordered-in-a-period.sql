-- # Write your MySQL query statement below
-- with cte as (
--     select p.product_id,p.product_name,o.order_date,o.unit from Products p join Orders o on p.product_id=o.product_id
--     where order_date between "2020-02-01" and "2020-02-28" 
-- )
-- select product_name,sum(unit) as unit from cte 
-- group by order_date
-- having sum(unit)>=100

SELECT 
    p.product_name, 
    SUM(o.unit) AS unit
FROM Products p
JOIN Orders o 
    ON p.product_id = o.product_id
WHERE o.order_date >= '2020-02-01' 
  AND o.order_date <= '2020-02-29'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;