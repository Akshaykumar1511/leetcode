# Write your MySQL query statement below
with cte as (
    select person_name,weight,turn,
    sum(weight) over (order by turn asc) as sm
    from Queue
)
select person_name from cte
where sm<=1000
order by turn Desc
limit 1;