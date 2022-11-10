-- MySQL

select S.score, dense_rank() over (
    order by S.score desc
  ) as 'rank'
FROM Scores as S;

--   Tests:
--1. Runtime 660 ms
--   Beats 22.55%
--2. Runtime 320 ms
--   Beats 77.97%