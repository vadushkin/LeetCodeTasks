-- MySQL

select u.name, ifnull(sum(r.distance),0) as travelled_distance
from users u left join rides r on u.id = r.user_id
group by u.id
order by travelled_distance desc, u.name asc

--   Tests:
--1. Runtime 970 ms
--   Beats 51.77%
--2. Runtime 1501 ms
--   Beats 16.53%
