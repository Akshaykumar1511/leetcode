# Write your MySQL query statement below

WITH cte AS (
    SELECT 
        departmentId,
        name AS Employee,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rn
    FROM Employee 
)

SELECT 
    d.name AS Department,
    c.Employee,
    c.salary AS Salary
FROM cte c
JOIN Department d ON c.departmentId = d.id
WHERE c.rn <= 3;