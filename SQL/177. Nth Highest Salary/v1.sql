-- MySQL

create FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N-1;
  RETURN (
      select distinct Salary from Employee order by Salary desc limit M, 1
  );
END

--   Tests:
--1. Runtime 421 ms
--   Beats 59.95%
--2. Runtime 468 ms
--   Beats 46.55%