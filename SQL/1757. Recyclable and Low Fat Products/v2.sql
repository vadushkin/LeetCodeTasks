-- Oracle

select product_id
from Products
where low_fats like 'Y%' and recyclable like 'Y%';

--   Tests:
--1. Runtime 761 ms
--   Beats 91.32%
--2. Runtime 837 ms
--   Beats 58.82%