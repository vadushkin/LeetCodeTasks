create table if not exists Department (
    id int,
    revenue int,
    month varchar(5)
);

Truncate table Department;

insert into Department (id, revenue, month)
values ('1', '8000', 'Jan');

insert into Department (id, revenue, month)
values ('2', '9000', 'Jan');

insert into Department (id, revenue, month)
values ('3', '10000', 'Feb');

insert into Department (id, revenue, month)
values ('1', '7000', 'Feb');

insert into Department (id, revenue, month)
values ('1', '6000', 'Mar');
