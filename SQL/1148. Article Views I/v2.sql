-- MySQL

select id
from (
    select author_id as id from Views
    where author_id = viewer_id
    order by id
) as a
group by id
order by id asc;

--   Tests:
--1. Runtime 566 ms
--   Beats 57.52%
--2. Runtime 570 ms
--   Beats 56.23%
