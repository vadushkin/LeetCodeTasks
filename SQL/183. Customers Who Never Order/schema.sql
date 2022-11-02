create table if not exists Customers (id int, name varchar(255));
create table if not exists Orders (id int, customerId int);

Truncate table Customers;

insert into Customers (id, name)
values ('1', 'Joe');
insert into Customers (id, name)
values ('2', 'Henry');
insert into Customers (id, name)
values ('3', 'Sam');
insert into Customers (id, name)
values ('4', 'Max');

Truncate table Orders;

insert into Orders (id, customerId)
values ('1', '3');
insert into Orders (id, customerId)
values ('2', '1');