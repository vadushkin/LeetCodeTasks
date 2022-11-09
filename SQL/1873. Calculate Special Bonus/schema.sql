create table if not exists Employees (
    employee_id int,
    name varchar(30),
    salary int
);

truncate table Employees;

insert into Employees (employee_id, name, salary)
values ('2', 'Meir', '3000');

insert into Employees (employee_id, name, salary)
values ('3', 'Michael', '3800');

insert into Employees (employee_id, name, salary)
values ('7', 'Addilyn', '7400');

insert into Employees (employee_id, name, salary)
values ('8', 'Juan', '6100');

insert into Employees (employee_id, name, salary)
values ('9', 'Kannon', '7700');
