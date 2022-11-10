-- MySQL

select S1.score,
  (
    select count(distinct S2.score)
    from Scores as S2
    where S2.score >= S1.score
  ) as 'rank'
from Scores as S1
order by S1.score desc;

--   Tests:
--1. Runtime 1196 ms
--   Beats 13.54%
--2. Runtime 1433 ms
--   Beats 5.1%