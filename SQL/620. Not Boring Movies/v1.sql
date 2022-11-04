-- MySQL

select *
from Cinema
where id % 2 = 1 and description != "boring"
order by rating desc;

--   Tests:
--1. Runtime 583 ms
--   Beats 5%
--2. Runtime 233 ms
--   Beats 71.19%