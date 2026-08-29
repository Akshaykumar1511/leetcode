# Write your MySQL query statement below
with cte as (select player_id, event_date as first_login, ROW_NUMBER() over (partition by player_id order by event_date) as rn
from Activity)

select player_id,first_login from cte where rn=1