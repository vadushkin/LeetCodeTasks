-- MySQL

select sell_date, count( distinct product ) as num_sold,
group_concat( distinct product order by product asc separator ',' ) as products
from Activities group by sell_date
order by sell_date asc;

--   Tests:
--1. Runtime 556 ms
--   Beats 60.41%
--2. Runtime 339 ms
--   Beats 99.92%
