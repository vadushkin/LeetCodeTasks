-- MySQL

delete p2
from Person as p1
JOIN Person as p2
ON p1.Email = p2.Email
where p1.id < p2.id;

--   Tests:
--1. Runtime: 1109 ms, faster than 51.39% of MySQL online submissions for Delete Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
--2. Runtime: 1123 ms, faster than 48.74% of MySQL online submissions for Delete Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.