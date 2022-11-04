-- MySQL

WITH rejected_ids AS (
    select s.product_id
    from sales as s
    where s.sale_date not between date('2019-01-01') and date('2019-03-31')
)

select distinct p.product_id, p.product_name
from product as p
inner join sales as s on s.product_id = p.product_id
left join rejected_ids as r on r.product_id = p.product_id
where s.sale_date between date('2019-01-01') and date('2019-03-31') and r.product_id is null

--   Tests:
--1. Runtime 1441 ms
--   Beats 92.74%
--2. Runtime 1594 ms
--   Beats 65.73%
