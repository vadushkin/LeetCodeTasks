-- MySQL

select *
from Patients
where conditions REGEXP '\\bDIAB1'

--   Tests:
--1. Runtime 929 ms
--   Beats 5.2%
--2. Runtime 555 ms
--   Beats 27.13%