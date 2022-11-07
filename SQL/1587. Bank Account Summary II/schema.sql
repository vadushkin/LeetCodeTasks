create table if not exists Users (
    account int,
    name varchar(20)
);

create table if not exists Transactions (
    trans_id int,
    account int,
    amount int,
    transacted_on date
);

truncate table Users;

insert into Users (account, name)
values ('900001', 'Alice');

insert into Users (account, name)
values ('900002', 'Bob');

insert into Users (account, name)
values ('900003', 'Charlie');

truncate table Transactions;

insert into Transactions (trans_id, account, amount, transacted_on)
values ('1', '900001', '7000', '2020-08-01');

insert into Transactions (trans_id, account, amount, transacted_on)
values ('2', '900001', '7000', '2020-09-01');

insert into Transactions (trans_id, account, amount, transacted_on)
values ('3', '900001', '-3000', '2020-09-02');

insert into Transactions (trans_id, account, amount, transacted_on)
values ('4', '900002', '1000', '2020-09-12');

insert into Transactions (trans_id, account, amount, transacted_on)
values ('5', '900003', '6000', '2020-08-07');

insert into Transactions (trans_id, account, amount, transacted_on)
values ('6', '900003', '6000', '2020-09-07');

insert into Transactions (trans_id, account, amount, transacted_on)
values ('7', '900003', '-4000', '2020-09-11');
