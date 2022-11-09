-- MySQL

select event_day as day, emp_id, sum(out_time) - sum(in_time) as total_time
from Employees
group by emp_id, event_day;

--   Tests:
--1. Runtime 661 ms
--   Beats 44.84%
--2. Runtime 486 ms
--   Beats 90.58%