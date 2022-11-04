-- MySQL

select s.name
from Orders o join Company c
on o.com_id = c.com_id
and c.name = 'RED'
right join SalesPerson s
on o.sales_id = s.sales_id
where o.sales_id is null;

--   Tests:
--1. Runtime 1199 ms
--   Beats 79.84%
--2. Runtime 1300 ms
--   Beats 68.88%