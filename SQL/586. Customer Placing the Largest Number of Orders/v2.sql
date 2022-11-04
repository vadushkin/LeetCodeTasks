-- MySQL

select customer_number
from (
    select customer_number, count(customer_number) as cnt
    from Orders
    group by customer_number
    order by cnt desc
    limit 1
) as Oak;

--   Tests:
--1. Runtime 1235 ms
--   Beats 5%
--2. Runtime 1269 ms
--   Beats 5%