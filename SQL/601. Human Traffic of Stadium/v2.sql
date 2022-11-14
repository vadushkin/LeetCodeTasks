-- MySQL

with q1 as (
select *, id - row_number() over() as id_diff
from stadium
where people > 99)

select id, visit_date, people
from q1
where id_diff in
    ( select id_diff
      from q1
      group by id_diff
      having count(*) > 2 )
order by visit_date;

--   Tests:
--1. Runtime 361 ms
--   Beats 77.10%
--2. Runtime 295 ms
--   Beats 98.96%