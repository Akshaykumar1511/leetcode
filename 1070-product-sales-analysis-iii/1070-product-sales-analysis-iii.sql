# Write your MySQL query statement below
with INTERMEDIATE AS (
    select product_id, year, quantity, price, dense_rank() over (partition by product_id order by year) as row_num
    from Sales
)
select product_id, year as first_year, quantity, price
from INTERMEDIATE
where row_num=1