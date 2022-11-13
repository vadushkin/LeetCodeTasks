-- MySQL

select id, 'Root' as Type
from Tree
where p_id is null

union

select id, 'Leaf' as Type
from Tree
where id not in (
        select distinct p_id
        from Tree
        where p_id is not null
        ) and p_id is not null

union

select id, 'Inner' as Type
from Tree
where id in (
        select distinct p_id
        from Tree
        where p_id is not null
        ) and p_id is not null

order by id;

--   Tests:
--1. Runtime 498 ms
--   Beats 61.50%
--2. Runtime 523 ms
--   Beats 54.74%