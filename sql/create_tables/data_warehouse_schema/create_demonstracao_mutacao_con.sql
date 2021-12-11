create table if not exists {schema}.demonstracao_mutacao_con
(
	cia_id int not null,
	ds_conta varchar(100),
	cd_conta varchar(18),
	vl_conta float,
	quarter varchar(10),
	COLUNA_DF CHAR(60),
	constraint fk_cia
        foreign key (cia_id) references {schema}.companies (id)
)