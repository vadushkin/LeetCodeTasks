-- MySQL

select activity_date as day, count(distinct user_id) as active_users
from Activity
where (activity_date > "2019-06-27" and activity_date <= "2019-07-27")
GROUP BY activity_date;

--   Tests:
--1. Runtime 712 ms
--   Beats 37.13%
--2. Runtime 651 ms
--   Beats 48.65%