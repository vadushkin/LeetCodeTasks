-- MySQL

select case
    when id mod 2 = 1 and id = (select max(id) from Seat) then id
    when id mod 2 = 1 then id + 1
    when id mod 2 = 0 then id - 1
    end as id, student
from Seat
order by id asc;

--   Tests:
--1. Runtime 495 ms
--   Beats 28.40%
--2. Runtime 323 ms
--   Beats 69.61%