-- MySQL

select customer_id, count(customer_id) as count_no_trans
from Visits as v left outer join Transactions as t
on v.visit_id = t.visit_id
where t.transaction_id is null
group by customer_id;

--   Tests:
--1. Runtime 1155 ms
--   Beats 91.23%
--2. Runtime 1463 ms
--   Beats 55.53%