-- MySQL

select name
from Customer
where referee_id != 2 or referee_id is Null;

--   Tests:
--1. Runtime 638 ms
--   Beats 44.41%
--2. Runtime 518 ms
--   Beats 77.9%