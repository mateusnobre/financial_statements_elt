create table if not exists {schema}.dfp_cia_aberta_DFC_MD_con
(
	cnpj_cia varchar(20),
    dt_refer varchar(10),
	versao varchar(30),
	denom_cia varchar(100),
    cd_cvm varchar(10),
	grupo_dfp varchar (206),
	moeda varchar(100),
	escala_moeda varchar(100),
	ordem_exerc varchar(9),
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1),
	ano int

)