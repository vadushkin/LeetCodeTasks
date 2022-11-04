-- MySQL

select *
from Cinema
where mod(id, 2) = 1 and description != 'boring'
order by rating desc;

--   Tests:
--1. Runtime 191 ms
--   Beats 97.92%
--2. Runtime 379 ms
--   Beats 21.36%