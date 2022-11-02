-- MySQL

select c.name as Customers
from Customers as c left outer join Orders as o
on c.id = o.customerId
where o.CustomerId is null;

--   Tests
--1. Runtime: 691 ms, faster than 36.38% of MySQL online submissions for Customers Who Never Order.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
--2. Runtime: 488 ms, faster than 79.45% of MySQL online submissions for Customers Who Never Order.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
