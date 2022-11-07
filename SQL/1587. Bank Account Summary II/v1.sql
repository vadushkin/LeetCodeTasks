-- MySQL

select u.name, sum(t.amount) as balance
from Users as u left outer join Transactions as t
on u.account = t.account
group by u.account
having balance > 10000;

--   Tests:
--1. Runtime 687 ms
--   Beats 77.5%
--2. Runtime 757 ms
--   Beats 64.8%