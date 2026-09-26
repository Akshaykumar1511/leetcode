# Write your MySQL query statement below
-- select customer_id, order_date, customer_pref_delivery_date
-- from Delivery
-- group by 
with INTERMEDIATE as (select customer_id, if(order_date=customer_pref_delivery_date,"immediate","scheduled") as del_type, ROW_NUMBER() over (partition by customer_id order by order_date asc) as row_num
from Delivery)

select round((sum(if(del_type='immediate',1,0))/count(del_type))*100,2) as immediate_percentage
from INTERMEDIATE
where row_num=1
