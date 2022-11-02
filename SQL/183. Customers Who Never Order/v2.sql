-- MySQL

select Customers.name as Customers
from Customers
where Customers.id not in
(
    select customerId from Orders
);

--   Tests:
--1. Runtime: 512 ms, faster than 72.74% of MySQL online submissions for Customers Who Never Order.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
--2. Runtime: 1112 ms, faster than 8.27% of MySQL online submissions for Customers Who Never Order.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.