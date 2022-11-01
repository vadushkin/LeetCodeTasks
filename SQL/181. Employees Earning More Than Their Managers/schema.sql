create table if not exists Employee (
    id int,
    name varchar(255),
    salary int,
    managerId int);

truncate table Employee;

insert into Employee (id, name, salary, managerId)
values ('1', 'Joe', '70000', '3');
insert into Employee (id, name, salary, managerId)
values ('2', 'Henry', '80000', '4');

insert into Employee (id, name, salary)
values ('3', 'Sam', '60000');
insert into Employee (id, name, salary)
values ('4', 'Max', '90000');
