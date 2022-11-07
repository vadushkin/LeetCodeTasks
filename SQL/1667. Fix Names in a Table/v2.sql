-- MySQL

select user_id, concat(upper(left(name, 1)), lower(right(name, length(name) - 1))) as name
from Users
order by user_id;

--   Tests:
--1. Runtime 722 ms
--   Beats 84.74%
--2. Runtime 824 ms
--   Beats 58.48%