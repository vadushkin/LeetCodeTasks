-- MySQL

update Salary
set sex =
case sex
    when 'm' then 'f'
    else 'm'
end;

--   Tests:
--1. Runtime 491 ms
--   Beats 13.68%
--2. Runtime 586 ms
--   Beats 6.63%