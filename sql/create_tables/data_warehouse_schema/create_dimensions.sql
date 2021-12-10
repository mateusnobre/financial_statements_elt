drop table if exists {schema}.companies;

create table {schema}.companies
(
    id    serial primary key,
    denom varchar(100),
    cnpj  varchar(20)
)