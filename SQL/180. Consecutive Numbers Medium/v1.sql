-- MySQL

select distinct l1.Num as ConsecutiveNums
from Logs as l1,
     Logs as l2,
     Logs as l3
where l1.Id = l2.Id - 1
      and l2.Id = l3.Id - 1
      and l1.Num = l2.Num
      and l2.Num = l3.Num;


--   Tests:
--1. Runtime 550 ms
--   Beats 69.72%
--2. Runtime 1033 ms
--   Beats 13.59%