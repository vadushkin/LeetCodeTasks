create table if not exists Seat (
    id int,
    student varchar(255)
);

truncate table Seat;

insert into Seat (id, student)
values ('1', 'Abbot');

insert into Seat (id, student)
values ('2', 'Doris');

insert into Seat (id, student)
values ('3', 'Emerson');

insert into Seat (id, student)
values ('4', 'Green');

insert into Seat (id, student)
values ('5', 'Jeames');
