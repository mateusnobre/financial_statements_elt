create table if not exists {schema}.itr_cia_aberta
(
   	cnpj_cia varchar(20),
	dt_refer varchar(10),
	versao varchar(30),
	denom_cia varchar(100),
   	cd_cvm varchar(10),
	categ_doc varchar(20),
	id_doc varchar(30),
	dt_receb varchar(10),
	link_doc varchar(121),
	ano int
)