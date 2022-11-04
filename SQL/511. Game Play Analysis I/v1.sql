-- MySQL

select player_id, min(event_date) as first_login
from Activity
group by player_id

--   Tests:
--1. Runtime 999 ms
--   Beats 22.31%
--2. Runtime 1065 ms
--   Beats 15.86%