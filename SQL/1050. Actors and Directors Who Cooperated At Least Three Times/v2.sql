-- MySQL

select actor_id, director_id
from (
select actor_id, director_id, count(timestamp) as cnt
from ActorDirector
group by actor_id, director_id
) as Oak
where cnt >= 3;

--   Tests:
--1. Runtime 598 ms
--   Beats 32.25%
--2. Runtime 405 ms
--   Beats 88.60%