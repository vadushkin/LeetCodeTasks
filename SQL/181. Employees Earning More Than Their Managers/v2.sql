-- MySQL

select e2.name as Employee
from Employee as e1 left outer join Employee as e2
on e1.id = e2.managerId
where e1.salary < e2.salary;


--   Tests
--1. Runtime: 443 ms, faster than 69.29% of MySQL online submissions for Employees Earning More Than Their Managers.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
--2. Runtime: 406 ms, faster than 81.59% of MySQL online submissions for Employees Earning More Than Their Managers.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
