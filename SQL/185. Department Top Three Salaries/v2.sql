-- MySQL

select Department, employee, salary
from (
     select d.name as Department,
            e.name as employee,
            e.salary,
            dense_rank() over (partition by d.name order by e.salary desc) as drk
    from Employee as e join Department as d
    on e.DepartmentId= d.Id
    ) as Oak
where Oak.drk <= 3;

--   Tests:
--1. Runtime 904 ms
--   Beats 69.73%
--2. Runtime 792 ms
--   Beats 83.43%