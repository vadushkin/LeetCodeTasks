-- MySQL

select name, population, area
from World
where area >= 3000000

union

select name, population, area
from World
where population >= 25000000;

--   Tests:
--1. Runtime 601 ms
--   Beats 8.84%
--2. Runtime 341 ms
--   Beats 97.42%