-- MySQL

select activity_date as day, count(distinct user_id) as active_users
from Activity
where datediff('2019-07-27', activity_date) < 30 and activity_date <= '2019-07-27'
group by activity_date;

--   Tests:
--1. Runtime 590 ms
--   Beats 66.64%
--2. Runtime 525 ms
--   Beats 89.24%