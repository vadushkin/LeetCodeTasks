-- MySQL

select Email
from Person
group by Email
having count(Email) > 1;

--   Tests
--1. Runtime: 448 ms, faster than 53.61% of MySQL online submissions for Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
--2. Runtime: 628 ms, faster than 24.59% of MySQL online submissions for Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
