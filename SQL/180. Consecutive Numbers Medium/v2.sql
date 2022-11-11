-- MySQL

select distinct Num as ConsecutiveNums
from Logs
where (Id + 1, Num) in (select * from Logs) and (Id + 2, Num) in (select * from Logs);

--   Tests:
--1. Runtime 1015 ms
--   Beats 14.60%
--2. Runtime 544 ms
--   Beats 71.35%