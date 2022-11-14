create table if not exists Employee (
    id int,
    name varchar(255),
    salary int,
    departmentId int
);

create table if not exists Department (
    id int,
    name varchar(255)
);

Truncate table Employee;

insert into Employee (id, name, salary, departmentId)
values ('1', 'Joe', '85000', '1');

insert into Employee (id, name, salary, departmentId)
values ('2', 'Henry', '80000', '2');

insert into Employee (id, name, salary, departmentId)
values ('3', 'Sam', '60000', '2');

insert into Employee (id, name, salary, departmentId)
values ('4', 'Max', '90000', '1');

insert into Employee (id, name, salary, departmentId)
values ('5', 'Janet', '69000', '1');

insert into Employee (id, name, salary, departmentId)
values ('6', 'Randy', '85000', '1');

insert into Employee (id, name, salary, departmentId)
values ('7', 'Will', '70000', '1');

Truncate table Department;

insert into Department (id, name)
values ('1', 'IT');

insert into Department (id, name)
values ('2', 'Sales');
