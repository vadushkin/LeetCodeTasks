-- MySQL

select date_id, make_name,
count(distinct lead_id) as unique_leads,
count(distinct partner_id) as unique_partners
from DailySales
group by date_id, make_name;

--   Tests:
--1. Runtime 1508 ms
--   Beats 5%
--2. Runtime1356 ms
--   Beats 5%