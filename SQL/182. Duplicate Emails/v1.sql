-- MySQL

select Email
from (
  select Email, count(Email) as num
  from Person
  group by Email
  ) as oak
where num > 1;

--   Tests
--1. Runtime: 369 ms, faster than 80.85% of MySQL online submissions for Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
--2. Runtime: 720 ms, faster than 15.88% of MySQL online submissions for Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
