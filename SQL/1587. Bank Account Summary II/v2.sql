-- MySQL

with tmp as(
    select t.account, u.name, sum(amount) as balance
    from Transactions as t
    left join Users as u
    on t.account = u.account
    group by account
)

select name, balance
from tmp
where balance > 10000;

--   Tests:
--1.Runtime 994 ms
--   Beats 34.84%
--2. Runtime 1144 ms
--   Beats 28.46%