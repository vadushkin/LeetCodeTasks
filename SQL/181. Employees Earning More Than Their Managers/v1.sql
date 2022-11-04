-- MySQL

select Name as Employee
from Employee as e1
where Salary > (
    select Salary
    from Employee as e2
    where e2.Id = e1.ManagerId
);

--   Tests
--1. Runtime: 1331 ms, faster than 8.23% of MySQL online submissions for Employees Earning More Than Their Managers.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
--2. Runtime: 1315 ms, faster than 8.82% of MySQL online submissions for Employees Earning More Than Their Managers.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
