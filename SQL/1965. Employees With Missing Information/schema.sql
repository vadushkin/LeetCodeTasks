create table if not exists Employees (
    employee_id int,
    name varchar(30)
);

create table if not exists Salaries (
    employee_id int,
    salary int
);

Truncate table Employees;

insert into Employees (employee_id, name)
values ('2', 'Crew');

insert into Employees (employee_id, name)
values ('4', 'Haven');

insert into Employees (employee_id, name)
values ('5', 'Kristian');

Truncate table Salaries;

insert into Salaries (employee_id, salary)
values ('5', '76071');

insert into Salaries (employee_id, salary)
values ('1', '22517');

insert into Salaries (employee_id, salary)
values ('4', '63539');
