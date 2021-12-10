create table if not exists {schema}.balanco_passivo_con
(
	cia_id int not null,
	ds_conta varchar(100),
	cd_conta varchar(18),
	vl_conta float,
	quarter varchar(10),
	dt_fim_exerc varchar(10),
	dt_refer varchar(10),
	constraint fk_cia
        foreign key (cia_id) references {schema}.companies (id)
)