# Create Schemas
```
CREATE SCHEMA financial_statements;
GO
CREATE SCHEMA dwh;
GO
```

## Create Tables cia_aberta

```
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

create table financial_statements.dfp_cia_aberta
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
```

## Create Tables BPA/BPP

```
create table financial_statements.itr_cia_aberta_bpa_con
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

create table financial_statements.itr_cia_aberta_bpa_ind

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

create table financial_statements.dfp_cia_aberta_bpa_con

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

create table financial_statements.dfp_cia_aberta_bpa_ind

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

create table financial_statements.itr_cia_aberta_bpp_con

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

create table financial_statements.itr_cia_aberta_bpp_ind
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

create table financial_statements.dfp_cia_aberta_bpp_con
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

create table financial_statements.dfp_cia_aberta_bpp_ind
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

```

## Create Tables DRE/DVA/DFC_MI/DFC_MD

```
create table financial_statements.dfp_cia_aberta_DRE_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.dfp_cia_aberta_DRE_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.itr_cia_aberta_DRE_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go
create table financial_statements.itr_cia_aberta_DRE_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.dfp_cia_aberta_DVA_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.dfp_cia_aberta_DVA_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.itr_cia_aberta_DVA_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go
create table financial_statements.itr_cia_aberta_DVA_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.dfp_cia_aberta_DFC_MI_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.dfp_cia_aberta_DFC_MI_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.itr_cia_aberta_DFC_MI_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go
create table financial_statements.itr_cia_aberta_DFC_MI_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.dfp_cia_aberta_DFC_MD_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.dfp_cia_aberta_DFC_MD_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go

create table financial_statements.itr_cia_aberta_DFC_MD_con
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go
create table financial_statements.itr_cia_aberta_DFC_MD_ind
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
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	cd_conta varchar(18),
    ds_conta varchar(100),
	vl_conta float,
	st_conta_fixa varchar(1)
)
go
```

## Create Tables DMPL

```
create table financial_statements.dfp_cia_aberta_DMPL_con
(
    cnpj_cia varchar(20),
    dt_refer varchar(10),
	versao text,
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
go

create table financial_statements.dfp_cia_aberta_DMPL_ind
(
    cnpj_cia varchar(20),
    dt_refer varchar(10),
	versao text,
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
go

create table financial_statements.itr_cia_aberta_DMPL_con
(
    cnpj_cia varchar(20),
    dt_refer varchar(10),
	versao text,
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
go

create table financial_statements.itr_cia_aberta_DMPL_ind
(
    cnpj_cia varchar(20),
    dt_refer varchar(10),
	versao text,
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
go
```

## Create Tables Balanços Ativo e Passivo

```
create table dwh.balanco_passivo_con
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

create table dwh.balanco_ativo_con
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

create table dwh.balanco_ativo_ind
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
```

## Create Tables Demonstração de Resultado do Exercício

```
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

create table dwh.demonstracao_resultado_ind
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
```

## Create Tables Demonstração do Valor Adicionado

```
create table dwh.demonstracao_valor_adicionado_con
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

create table dwh.demonstracao_valor_adicionado_ind
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
```

## Create Tables Demonstração de Fluxo de Caixa - Método Direto

```
create table dwh.demonstracao_fluxo_direto_con
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

create table dwh.demonstracao_fluxo_direto_ind
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
```

## Create Tables Demonstração de Fluxo de Caixa - Método Indireto

```
create table dwh.demonstracao_fluxo_indireto_con
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

create table dwh.demonstracao_fluxo_indireto_ind
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
```

## Create Tables Demonstração de Mutação do Patrimônio Líquido

```
create table dwh.demonstracao_mutacao_con
(
	cnpj_cia varchar(20),
	denom_cia varchar(100),
	ds_conta varchar(100),
	cd_conta varchar(18),
	vl_conta float,
	quarter varchar(10),
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	COLUNA_DF CHAR(60)
)
go

create table dwh.demonstracao_mutacao_ind
(
	cnpj_cia varchar(20),
	denom_cia varchar(100),
	ds_conta varchar(100),
	cd_conta varchar(18),
	vl_conta float,
	quarter varchar(10),
	dt_ini_exerc varchar(10),
	dt_fim_exerc varchar(10),
	COLUNA_DF CHAR(60)
)
go
```

## Create Table Cias Abertas

```
create table dwh.cias_abertas
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
```