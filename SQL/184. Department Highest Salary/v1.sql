-- MySQL

select Department.name as Department,
       Employee.name as Employee,
       Salary
from Employee join Department
on Employee.DepartmentId = Department.Id
where (Employee.DepartmentId, Salary) in
    (
    select DepartmentId, max(Salary)
    from Employee
    group by DepartmentId
    );

--   Tests:
--1. Runtime 1552 ms
--   Beats 7.59%
--2. Runtime 610 ms
--   Beats 84.34%