-- MySQL

select class
from (
    select class, count(class) as cnt
    from Courses
    group by class) as Oak
where cnt >= 5;

--   Tests:
--1. Runtime 393 ms
--   Beats 55.82%
--2. Runtime 619 ms
--   Beats 12.95%