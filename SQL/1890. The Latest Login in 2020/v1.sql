-- MySQL

select user_id, max(time_stamp) as last_stamp
from Logins
where year(time_stamp) = 2020
group by user_id;

--   Tests:
--1. Runtime 833 ms
--   Beats 45.72%
--2. Runtime 1150 ms
--   Beats 20.14%