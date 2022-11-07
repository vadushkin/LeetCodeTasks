-- MySQL

select customer_id, count(visit_id) as count_no_trans
from Visits
where visit_id not in (
	select visit_id from Transactions
	)
group by customer_id;

--   Tests:
--1. Runtime 1796 ms
--   Beats 34.32%
--2. Runtime 1860 ms
--   Beats 31.19%