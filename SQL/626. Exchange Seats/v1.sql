-- MySQL

select IF(S.id + 1 in (select id from Seat),
       IF(S.id % 2 = 0, S.id - 1, S.id + 1),
       IF(S.id % 2 = 1, S.id, S.id - 1)) as id,
       S.student
FROM Seat as S
ORDER BY id;


--   Tests:
--1. Runtime 335 ms
--   Beats 65.18%
--2. Runtime 724 ms
--   Beats 7.3%