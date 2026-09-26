# Write your MySQL query statement below
-- select count(distinct player_id) 
-- from Activity
with INTERMEDIATE AS (select player_id,device_id,event_date, Lead(event_date) over (partition by player_id order by event_date) as next_event_date, row_number() over (partition by player_id order by event_date) as row_num
from Activity)

-- select PLAYER_ID , event_date,next_event_date  FROM INTERMEDIATE where row_num=1

select round(avg(if(next_event_date=event_date+interval 1 day,1,0)),2) as fraction FROM INTERMEDIATE where row_num=1