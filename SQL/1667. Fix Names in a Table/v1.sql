-- MySQL

select user_id, concat(upper(substr(name, 1, 1)), lower(substr(name, 2))) as name
from Users
order by user_id asc;

--   Tests:
--1. Runtime N/A (552 ms)
--   Beats N/A (99.94%)
--2. Runtime 685 ms
--   Beats 94.46%