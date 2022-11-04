-- MySQL

select class
from Courses
group by class
having count(distinct student) >= 5;

--   Tests:
--1. Runtime 345 ms
--   Beats 78.89%
--2. Runtime 566 ms
--   Beats 18.41%