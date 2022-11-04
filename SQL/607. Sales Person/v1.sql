-- MySQL

select name
from SalesPerson
where sales_id not in (
    select sales_id
    from Orders as o left outer join Company as c
    on c.com_id = o.com_id
    where c.name = "RED"
);

--   Tests:
--1. Runtime 1602 ms
--   Beats 44.74%
--2. Runtime 1478 ms
--   Beats 52.60%