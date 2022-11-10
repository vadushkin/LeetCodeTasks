-- MySQL

select (
    case
        when count(Oak.salary) = 2 then sum(Oak.salary) - Oak.salary
        else null
    end
) as SecondHighestSalary
from (
    select distinct salary
    from employee
    order by salary desc
    limit 2
) as Oak;

--   Tests:
--1. Runtime 265 ms
--   Beats 68.90%
--2. Runtime 409 ms
--   Beats 22.99%