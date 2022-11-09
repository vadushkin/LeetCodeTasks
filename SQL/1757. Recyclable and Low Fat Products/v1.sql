-- MySQL

select product_id
from Products
where low_fats = "Y" and recyclable = "Y";

--   Tests:
--1. Runtime 525 ms
--   Beats 80.72%
--2. Runtime 463 ms
--   Beats 96.84%