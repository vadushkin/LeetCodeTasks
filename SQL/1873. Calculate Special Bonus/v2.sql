-- MySQL

select employee_id,
case
    when employee_id % 2 != 0 and name NOT LIKE 'M%' then salary
    else 0
end as bonus
from Employees
order by employee_id;

--   Tests:
--1. Runtime 1622 ms
--   Beats 5%
--2. Runtime 715 ms
--   Beats 63.80%