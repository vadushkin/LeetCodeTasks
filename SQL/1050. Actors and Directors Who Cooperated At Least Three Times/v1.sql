-- MySQL

select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(timestamp) >= 3;

--   Tests:
--1. Runtime 490 ms
--   Beats 54.75%
--2. Runtime 636 ms
--   Beats 26.54%