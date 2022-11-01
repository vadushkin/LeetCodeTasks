-- MySQL

select p.firstName, p.lastName, a.city, a.state
from Person as p left outer join Address as a
on p.personId = a.personId;

--   Tests:
--1. Runtime: 386 ms, faster than 89.71% of MySQL online submissions for Combine Two Tables.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
--2. Runtime: 474 ms, faster than 58.67% of MySQL online submissions for Combine Two Tables.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.