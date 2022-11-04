-- MySQL

select distinct(author_id) as id
from Views
where author_id = viewer_id
order by id asc;

--   Tests:
--1. Runtime 738 ms
--   Beats 26.76%
--2. Runtime 618 ms
--   Beats 43.17%