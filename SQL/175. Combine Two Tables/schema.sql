create table if not exists Person (
    personId int,
    firstName varchar(255),
    lastName varchar(255)
    );
create table if not exists Address (
    addressId int,
    personId int,
    city varchar(255),
    state varchar(255)
    );

truncate table Person;

insert into Person (personId, lastName, firstName)
values ('1', 'Wang', 'Allen');
insert into Person (personId, lastName, firstName)
values ('2', 'Alice', 'Bob');

truncate table Address;

insert into Address (addressId, personId, city, state)
values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state)
values ('2', '3', 'Leetcode', 'California');
