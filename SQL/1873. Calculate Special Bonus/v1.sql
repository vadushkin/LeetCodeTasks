-- MySQL

select employee_id, if(employee_id % 2 = 1 and name not like "M%", salary, 0) as bonus
from Employees
order by employee_id asc;

--   Tests:
--1. Runtime 1166 ms
--   Beats 15.87%
--2. Runtime 590 ms
--   Beats 94.93%