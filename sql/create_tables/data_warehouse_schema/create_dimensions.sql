create table if not exists {schema}.companies
(
    id    serial primary key,
    denom varchar(100),
    cnpj  varchar(20)
)