-- MySQL

create function getNthHighestSalary(N int) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      SELECT DISTINCT(salary) from Employee order by salary DESC
      LIMIT 1 OFFSET N
  );
END

--   Tests:
--1. Runtime 677 ms
--   Beats 20.99%
--2. Runtime 436 ms
--   Beats 54.76%