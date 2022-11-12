-- MySQL

select Oak.employee_id
from (
     select * from Employees left join Salaries using(employee_id)
     union
     select * from Employees right join Salaries using(employee_id)
     ) as Oak
where Oak.salary is null or Oak.name is null
order by employee_id;

--   Tests:
--1. Runtime 446 ms
--   Beats 98.67%
--2. Runtime 438 ms
--   Beats 99.22%