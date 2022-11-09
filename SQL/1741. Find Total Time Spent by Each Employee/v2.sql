-- MySQL

select event_day as day, emp_id, sum(out_time-in_time) as total_time
from Employees
group by event_day, emp_id;

--   Tests:
--1. Runtime 1034 ms
--   Beats 13.8%
--2. Runtime 758 ms
--   Beats 32.99%