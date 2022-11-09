-- MSSQL

select product_id, store, price
from Products
unpivot (
    price for store in (store1, store2, store3)
) as T;

--   Tests:
--1. Runtime 714 ms
--   Beats 66.26%
--2. Runtime 716 ms
--   Beats 65.24%