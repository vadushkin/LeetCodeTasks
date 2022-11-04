create table if not exists Orders (
    order_number int,
    customer_number int
 );

Truncate table Orders;

insert into Orders (order_number, customer_number)
values ('1', '1');

insert into Orders (order_number, customer_number)
values ('2', '2');

insert into Orders (order_number, customer_number)
values ('3', '3');

insert into Orders (order_number, customer_number)
values ('4', '3')
;