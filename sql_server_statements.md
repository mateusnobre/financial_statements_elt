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