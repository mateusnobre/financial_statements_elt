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


**create balanco_ativo_ind**

create table financial_statements.balanco_ativo_ind
(
	cnpj_cia text,
	denom_cia text,
	ds_conta text,
	valor_2011_q1 float,
    valor_2012_q1 float,
	valor_2013_q1 float,
	valor_2014_q1 float,
	valor_2015_q1 float,
	valor_2016_q1 float,
	valor_2017_q1 float,
	valor_2018_q1 float,
	valor_2019_q1 float,
	valor_2020_q1 float,
	valor_2021_q1 float,
    valor_2022_q1 float,
	valor_2011_q2 float,
    valor_2012_q2 float,
	valor_2013_q2 float,
	valor_2014_q2 float,
	valor_2015_q2 float,
	valor_2016_q2 float,
	valor_2017_q2 float,
	valor_2018_q2 float,
	valor_2019_q2 float,
	valor_2020_q2 float,
	valor_2021_q2 float,
    valor_2022_q2 float,
	valor_2011_q3 float,
    valor_2012_q3 float,
	valor_2013_q3 float,
	valor_2014_q3 float,
	valor_2015_q3 float,
	valor_2016_q3 float,
	valor_2017_q3 float,
	valor_2018_q3 float,
	valor_2019_q3 float,
	valor_2020_q3 float,
	valor_2021_q3 float,
    valor_2022_q3 float,
	valor_2011_q4 float,
    valor_2012_q4 float,
	valor_2013_q4 float,
	valor_2014_q4 float,
	valor_2015_q4 float,
	valor_2016_q4 float,
	valor_2017_q4 float,
	valor_2018_q4 float,
	valor_2019_q4 float,
	valor_2020_q4 float,
	valor_2021_q4 float,
    valor_2022_q4 float
) 
go

**create balanco_passivo_ind**

create table financial_statements.balanco_passivo_ind
(
	cnpj_cia text,
	denom_cia text,
	ds_conta text,
	valor_2011_q1 float,
    valor_2012_q1 float,
	valor_2013_q1 float,
	valor_2014_q1 float,
	valor_2015_q1 float,
	valor_2016_q1 float,
	valor_2017_q1 float,
	valor_2018_q1 float,
	valor_2019_q1 float,
	valor_2020_q1 float,
	valor_2021_q1 float,
    valor_2022_q1 float,
	valor_2011_q2 float,
    valor_2012_q2 float,
	valor_2013_q2 float,
	valor_2014_q2 float,
	valor_2015_q2 float,
	valor_2016_q2 float,
	valor_2017_q2 float,
	valor_2018_q2 float,
	valor_2019_q2 float,
	valor_2020_q2 float,
	valor_2021_q2 float,
    valor_2022_q2 float,
	valor_2011_q3 float,
    valor_2012_q3 float,
	valor_2013_q3 float,
	valor_2014_q3 float,
	valor_2015_q3 float,
	valor_2016_q3 float,
	valor_2017_q3 float,
	valor_2018_q3 float,
	valor_2019_q3 float,
	valor_2020_q3 float,
	valor_2021_q3 float,
    valor_2022_q3 float,
	valor_2011_q4 float,
    valor_2012_q4 float,
	valor_2013_q4 float,
	valor_2014_q4 float,
	valor_2015_q4 float,
	valor_2016_q4 float,
	valor_2017_q4 float,
	valor_2018_q4 float,
	valor_2019_q4 float,
	valor_2020_q4 float,
	valor_2021_q4 float,
    valor_2022_q4 float
) 
go
