-- MySQL

select
    Ids.id,
    January.revenue as Jan_Revenue,
    Feburary.revenue as Feb_Revenue,
    March.revenue as Mar_Revenue,
    April.revenue as Apr_Revenue,
    May.revenue as May_Revenue,
    June.revenue as Jun_Revenue,
    July.revenue as Jul_Revenue,
    August.revenue as Aug_Revenue,
    September.revenue as Sep_Revenue,
    October.revenue as Oct_Revenue,
    November.revenue as Nov_Revenue,
    December.revenue as Dec_Revenue
from
    (
    select distinct
      id
    from
      Department
    ) as Ids
        left join Department as January on (
        Ids.id = January.id
        and January.month = "Jan"
    )
        LEFT JOIN Department AS Feburary ON (
        Ids.id = Feburary.id
        and Feburary.month = "Feb"
    )
        LEFT JOIN Department AS March ON (
        Ids.id = March.id
        AND March.month = "Mar"
    )
        LEFT JOIN Department AS April ON (
        Ids.id = April.id
        AND April.month = "Apr"
    )
        LEFT JOIN Department AS May ON (
        Ids.id = May.id
        AND May.month = "May"
    )
        LEFT JOIN Department AS June ON (
        Ids.id = June.id
        AND June.month = "Jun"
    )
        LEFT JOIN Department AS July ON (
        Ids.id = July.id
        AND July.month = "Jul"
    )
        LEFT JOIN Department AS August ON (
        Ids.id = August.id
        AND August.month = "Aug"
    )
        LEFT JOIN Department AS September ON (
        Ids.id = September.id
        AND September.month = "Sep"
    )
        LEFT JOIN Department AS October ON (
        Ids.id = October.id
        AND October.month = "Oct"
    )
        LEFT JOIN Department AS November ON (
        Ids.id = November.id
        AND November.month = "Nov"
    )
        LEFT JOIN Department AS December ON (
        Ids.id = December.id
        AND December.month = "Dec"
    );

--   Tests:
--1. Runtime 615 ms
--   Beats 85.5%
--2. Runtime 1180 ms
--   Beats 7.88%