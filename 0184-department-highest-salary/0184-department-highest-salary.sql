# Write your MySQL query statement below
with cte as (
    select d.name as Department,e.name as Employee,e.salary as Salary, dense_rank() over (partition by e.departmentId order by e.salary desc) as ds
    from Employee e
    join Department d on d.id=e.DepartmentId
)
select Department, Employee, Salary from cte where ds=1