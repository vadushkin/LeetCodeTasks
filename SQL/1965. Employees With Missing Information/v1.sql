-- MySQL

select employee_id
from Employees
where employee_id not in (select employee_id from Salaries)

union

select employee_id
from Salaries
where employee_id not in (select employee_id from Employees)
order by employee_id asc;

--   Tests:
--1. Runtime 3138 ms
--   Beats 5.1%
--2. Runtime 431 ms
--   Beats 99.57%