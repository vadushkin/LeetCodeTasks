-- MySQL

select product_id, product_name
from Sales join Product using(product_id)
group by product_id
having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31';

--   Tests:
--1. Runtime 1810 ms
--   Beats 40.62%
--2. Runtime 1792 ms
--   Beats 42%