-- MySQL

select user_id, max(time_stamp) as last_stamp
from logins
where time_stamp like '2020%'
group by user_id;

--   Tests:
--1. Runtime 1148 ms
--   Beats 20.36%
--2. Runtime 779 ms
--   Beats 56.54%