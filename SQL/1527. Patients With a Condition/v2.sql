-- MySQL

select *
from Patients
where conditions like '% DIAB1%' or conditions like 'DIAB1%';

--   Tests:
--1. Runtime 338 ms
--   Beats 77.62%
--2. Runtime 903 ms
--   Beats 5.2%