-- MSSQL

select  date_id,
        make_name,
        count(distinct lead_id) as unique_leads,
        count(distinct partner_id) as unique_partners
from DailySales
group by date_id, make_name;

--   Tests:
--1. Runtime 799 ms
--   Beats 86.39%
--2. Runtime 966 ms
--   Beats 43.12%