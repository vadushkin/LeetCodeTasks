"""Table: DailySales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
This table does not have a primary key.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.


Write an SQL query that will, for each date_id and make_name,
return the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

The query result format is in the following example."""