-- MySQL

select stock_name, sum(summary) as capital_gain_loss
from (
     select stock_name, operation, if(operation = "Buy", sum(price) * -1, sum(price) as summary
     from Stocks
     group by stock_name, operation
     ) as Oak
group by stock_name;

--   Tests:
--1. Runtime 662 ms
--   Beats 54.45%
--2. Runtime 651 ms
--   Beats 57.44%