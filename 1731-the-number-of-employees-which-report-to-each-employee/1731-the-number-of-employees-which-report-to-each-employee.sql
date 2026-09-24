# Write your MySQL query statement below
-- with manager_stats as (select reports_to as employee_id, name ,count(reports_to) as reports_count, round(avg(age),0) as average_age
-- from employees
-- where reports_to is not null
-- group by reports_to)

-- select e.employee_id, e.name,m.reports_count,m.average_age
-- from employees e
-- join manager_stats m on m.employee_id=e.employee_id
-- order by e.employee_id

select e.employee_id, e.name, count(m.employee_id) as reports_count, round(avg(m.age),0) as average_age
from Employees e
join Employees m on e.employee_id=m.reports_to
group by e.employee_id,e.name
order by e.employee_id