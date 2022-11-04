-- MySQL

select distinct
  A.player_id,
  first_value(A.event_date) over (
    partition by
      A.player_id
    order by
      A.event_date
  ) as first_login
from
  Activity A;

--   Tests:
--1. Runtime 713 ms
--   Beats 72.46%
--2. Runtime 820 ms
--   Beats 41.67%