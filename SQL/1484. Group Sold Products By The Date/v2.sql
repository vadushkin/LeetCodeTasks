-- MS SQL Server

select a.sell_date,
    count(a.product) as num_sold,
    string_agg(a.product,',') within group (
    order by a.product) products
    from (select distinct sell_date, product from activities) as a
group by a.sell_date
order by a.sell_date;

--   Tests:
--1. Runtime 1769 ms
--   Beats 47.94%
--2. Runtime 4564 ms
--   Beats 5.11%