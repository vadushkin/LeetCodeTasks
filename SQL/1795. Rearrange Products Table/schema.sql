create table if not exists Products (
    product_id int,
    store1 int,
    store2 int,
    store3 int
);

truncate table Products;

insert into Products (product_id, store1, store2, store3)
values ('0', '95', '100', '105');

insert into Products (product_id, store1, store2, store3)
values ('1', '70', null, '80');
