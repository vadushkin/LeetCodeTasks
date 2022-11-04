--  MySQL

select name, population, area
from World
where area >= 3000000 or population >= 25000000;

--   Tests:
--1. Runtime 650 ms
--   Beats 5.94%
--2. Runtime 383 ms
--   Beats 69.98%
