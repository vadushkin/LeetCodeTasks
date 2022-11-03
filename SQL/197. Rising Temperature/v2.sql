-- MySQL

select weather.id as Id
from weather
join weather as w
on datediff(weather.recordDate, w.recordDate) = 1
and weather.Temperature > w.Temperature;

--   Tests:
--1. Runtime: 1119 ms, faster than 21.71% of MySQL online submissions for Rising Temperature.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.
--2. Runtime: 865 ms, faster than 65.46% of MySQL online submissions for Rising Temperature.
--   Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.