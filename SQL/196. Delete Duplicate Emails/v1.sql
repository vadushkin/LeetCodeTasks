-- MySQL

delete from Person
where id not in (
select * from (
select min(id)
from Person
group by email) as oak);

--   Tests:
--1. Runtime: 482 ms, faster than 99.60% of MySQL online submissions for Delete Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
--2. Runtime: 449 ms, faster than 99.97% of MySQL online submissions for Delete Duplicate Emails.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
