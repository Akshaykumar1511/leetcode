# Write your MySQL query statement below
-- select case 
-- when id%2=1 and (select max(id) from Seat)=id then id
-- when id%2=1 then id+1
-- else id-1
-- end as id, student
-- from Seat
-- order by id

select id,ifnull(case
when id%2=0 then lag(student) over (order by id)
else lead(student) over (order by id) end
,student) as student
from Seat