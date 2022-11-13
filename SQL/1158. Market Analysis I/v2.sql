-- MySQL

select U.user_id as buyer_id, U.join_date, count(O.order_id) as orders_in_2019
from Users as U
left join (
          select * from Orders
          where YEAR(order_date) = 2019
          ) as O on (U.user_id = O.buyer_id)
group by U.user_id;

--   Tests:
--1. Runtime 2144 ms
--   Beats 19.72%
--2. Runtime 2075 ms
--   Beats 22.95%