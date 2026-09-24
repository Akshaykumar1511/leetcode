# Write your MySQL query statement below
with manager_stats as (select reports_to as employee_id, name ,count(reports_to) as reports_count, round(avg(age),0) as average_age
from employees
where reports_to is not null
group by reports_to)

select e.employee_id, e.name,m.reports_count,m.average_age
from employees e
join manager_stats m on m.employee_id=e.employee_id
order by e.employee_id


-- SELECT 
--     m.employee_id, 
--     m.name, 
--     COUNT(e.employee_id) AS reports_count, 
--     ROUND(AVG(e.age), 0) AS average_age
-- FROM Employees e
-- JOIN Employees m ON e.reports_to = m.employee_id
-- GROUP BY m.employee_id, m.name
-- ORDER BY m.employee_id;