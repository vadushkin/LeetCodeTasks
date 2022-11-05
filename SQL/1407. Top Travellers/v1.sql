-- MySQL

select name,
    sum(case when u.id = r.user_id then distance
    else 0 end) as travelled_distance
from users as u
left outer join rides as r
on u.id = r.user_id
group by u.id
order by sum(distance) desc, name asc;

--   Tests:
--1. Runtime 973 ms
--   Beats 51.28%
--2. Runtime 1697 ms
--   Beats 9.55%