create table if not exists {schema}.dfp_cia_aberta_DMPL_con
(
    cnpj_cia varchar(20),
    dt_refer varchar(10),
	versao varchar(30),
	denom_cia varchar(100),
    cd_cvm varchar(10),
	grupo_dfp varchar (206),
	moeda varchar(100),
	escala_moeda varchar(100),
	ORDEM_EXERC VARCHAR(9),
	DT_INI_EXERC VARCHAR(10),
	DT_FIM_EXERC VARCHAR(10),
	COLUNA_DF CHAR(60),
	CD_CONTA VARCHAR(18),
	DS_CONTA VARCHAR(100),
	VL_CONTA float,
	ST_CONTA_FIXA VARCHAR,
	ano int
)