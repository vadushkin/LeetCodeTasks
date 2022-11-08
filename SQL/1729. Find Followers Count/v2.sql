-- MySQL

select user_id , count(distinct follower_id) as followers_count
from Followers
group by user_id;

--   Tests:
--1. Runtime 910 ms
--   Beats 27.12%
--2. Runtime 544 ms
--   Beats 87.46%