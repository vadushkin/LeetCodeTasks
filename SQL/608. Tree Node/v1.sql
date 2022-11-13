-- MySQL

select id, if(ISNULL(p_id),
              'Root',
              if(id in (select p_id from Tree),
                 'Inner',
                 'Leaf')
              ) as Type
from Tree order by id;

--   Tests:
--1. Runtime 846 ms
--   Beats 17.26%
--2. Runtime 590 ms
--   Beats 39.76%