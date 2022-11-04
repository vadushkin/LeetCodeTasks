-- MySQL

select customer_number
from Orders
group by customer_number
order by count(order_number) desc
limit 1;

--   Tests:
--1. Runtime 385 ms
--   Beats 99.88%
--2. Runtime 541 ms
--   Beats 61.61%
