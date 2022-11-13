-- MySQL

select U.user_id as buyer_id, U.join_date, count(O.order_id) as orders_in_2019
from Users as U left join Orders as O
on O.buyer_id = U.user_id and YEAR(order_date) = 2019
group by U.user_id;

--   Tests:
--1. Runtime 1232 ms
--   Beats 87.78%
--2. Runtime 1163 ms
--   Beats 96.56%
