create table if not exists Person (
    Id int,
    Email varchar(255)
);

truncate table Person;

insert into Person (id, email)
values ('1', 'john@example.com');

insert into Person (id, email)
values ('2', 'bob@example.com');

insert into Person (id, email)
values ('3', 'john@example.com');