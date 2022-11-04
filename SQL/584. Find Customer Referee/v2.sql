-- MySQL

select name
from Customer
where coalesce(referee_id, '') != 2

--   Tests:
--1. Runtime 725 ms
--   Beats 33.11%
--2. Runtime 571 ms
--   Beats 61.47%