# Write your MySQL query statement below
with cte as (
    select num, 
    LEAD(num,1) over (order by id) as next_1,
    LEAD(num,2) over(order by id) as next_2
    from Logs
)

select distinct num as ConsecutiveNums from cte
where num=next_1 and num=next_2