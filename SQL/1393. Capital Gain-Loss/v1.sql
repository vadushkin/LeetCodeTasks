-- MySQL

select stock_name, sum(price) as capital_gain_loss
from (
     select stock_name, IF(operation = "Buy", summary * -1, summary) as price
     from (
          select stock_name, operation, sum(price) as summary
          from Stocks
          group by stock_name, operation
          ) as Oak
     ) as Oak2
group by stock_name;

--   Tests:
--1. Runtime 541 ms
--   Beats 90.42%
--2. Runtime 642 ms
--   Beats 59.75%