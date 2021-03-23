**create itr_cia_aberta**

create table financial_statements.itr_cia_aberta
(
   	cnpj_cia varchar(20),
	dt_refer varchar(10),
	versao text,
	denom_cia varchar(100),
   	cd_cvm varchar(10),
	categ_doc varchar(20),
	id_doc text,
	dt_receb varchar(10),
	link_doc varchar(121)
)
go

**create itr_cia_aberta_bpa_consolidado**

create table financial_statements.itr_cia_aberta_bpa_consolidado
(
    cnpj_cia varchar(20),
    dt_refer varchar(10),
	versao text,
	denom_cia varchar(100),
    cd_cvm varchar(10),
	grupo_dfp varchar (206),
	moeda varchar(100),
	escala_moeda varchar(100),
	ordem_exerc varchar(9),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

**create financial_statements.dfp_cia_aberta_DRE_con**


create table financial_statements.dfp_cia_aberta_DRE_con
(
	CD_CONTA VARCHAR(18),
	CD_CVM CHAR(6),
	CNPJ_CIA VARCHAR(20),
	DENOM_CIA VARCHAR(100),
	DS_CONTA VARCHAR(100),
	DT_FIM_EXERC VARCHAR(10),
	DT_INI_EXERC VARCHAR(10),
	DT_REFER VARCHAR(10),
	ESCALA_MOEDA VARCHAR(100),
	GRUPO_DFP VARCHAR(206),
	MOEDA VARCHAR(100),
	ORDEM_EXERC VARCHAR(9),
	ST_CONTA_FIXA VARCHAR,
	VERSAO INT,
	VL_CONTA float,
	ano int
)
go

**create balanco_passivo_ind**


create table dwh.balanco_passivo_ind
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
go

**create demonstracao_resultado_con**

create table dwh.demonstracao_resultado_con
(
	cnpj_cia varchar(20),
	denom_cia varchar(100),
	ds_conta varchar(100),
	cd_conta varchar(18),
	vl_conta float,
	quarter varchar(10),
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10)
)
go