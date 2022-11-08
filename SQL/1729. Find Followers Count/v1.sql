-- MySQL

select user_id, count(follower_id) as followers_count
from Followers
group by user_id
order by user_id;

--   Tests:
--1. Runtime 1078 ms
--   Beats 14.12%
--2. Runtime 514 ms
--   Beats 95.35%