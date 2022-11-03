-- MySQL

select w1.Id
from weather w1, weather w2
where to_days(w1.RecordDate) - to_days(w2.RecordDate) = 1
and w1.Temperature > w2.Temperature;

--   Tests:
--1. Runtime: 1385 ms, faster than 6.99% of MySQL online submissions for Rising Temperature.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.
--2. Runtime: 797 ms, faster than 73.14% of MySQL online submissions for Rising Temperature.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.