-- MySQL

select d.name as Department ,e.name as Employee, e.salary
from Employee as e, Department as d
where e.DepartmentId = d.id and (DepartmentId, Salary) in
(
    select DepartmentId, max(Salary) as max
    from Employee
    group by DepartmentId
);

--   Tests:
--1. Runtime 789 ms
--   Beats 50.12%
--2. Runtime 906 ms
--   Beats 38.88%