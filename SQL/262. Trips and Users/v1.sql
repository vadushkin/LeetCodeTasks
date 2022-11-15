-- MySQL

select request_at as Day,
       round(count(
             case
             when status != 'completed' then 1
             else null
             end) / count(*), 2) as "Cancellation Rate"
from Trips

inner join Users client on client.users_id = Trips.client_id
inner join Users driver on driver.users_id = Trips.driver_id

where client.banned = 'No'
and driver.banned = 'No'
and request_at >= "2013-10-01"
and request_at <= "2013-10-03"

group by request_at;

--   Tests:
--1. Runtime 560 ms
--   Beats 67.28%
--2. Runtime 434 ms
--   Beats 98.44%
