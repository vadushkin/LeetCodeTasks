-- MySQL

update Salary
set sex = if(sex='f', 'm', 'f');

--   Tests:
--1. Runtime 293 ms
--   Beats 60.4%
--2. Runtime 463 ms
--   Beats 17.9%