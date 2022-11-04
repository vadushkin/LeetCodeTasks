-- MySQL

select p.firstName, p.lastName, a.city, a.state
from Person p left join Address a
using (personId);

--   Tests:
--1. Runtime: 398 ms, faster than 84.99% of MySQL online submissions for Combine Two Tables.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
--2. Runtime: 455 ms, faster than 64.80% of MySQL online submissions for Combine Two Tables.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.