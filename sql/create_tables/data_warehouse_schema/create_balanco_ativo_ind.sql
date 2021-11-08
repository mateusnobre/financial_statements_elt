create table if not exists {schema}.balanco_ativo_ind
(
	cnpj_cia varchar(20),
	denom_cia varchar(100),
	ds_conta varchar(100),
	cd_conta varchar(18),
	vl_conta float,
	quarter varchar(10),
	dt_fim_exerc varchar(10),
	dt_refer varchar(10)
)