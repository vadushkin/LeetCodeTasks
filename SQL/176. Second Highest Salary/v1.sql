-- MySQL

select max(salary) as SecondHighestSalary
from Employee
where salary != (
    select max(salary)
    from Employee
);

--   Tests:
--1. Runtime 362 ms
--   Beats 34.58%
--2. Runtime 362 ms
--   Beats 34.58%