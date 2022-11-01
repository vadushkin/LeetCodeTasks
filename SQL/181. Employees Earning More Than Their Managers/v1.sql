-- MySQL

select Name as Employee from Employee e
where Salary > (
    select Salary from Employee m where m.Id = e.ManagerId
)


--   Tests
--1. Runtime: 1331 ms, faster than 8.23% of MySQL online submissions for Employees Earning More Than Their Managers.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
--2. Runtime: 1315 ms, faster than 8.82% of MySQL online submissions for Employees Earning More Than Their Managers.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
