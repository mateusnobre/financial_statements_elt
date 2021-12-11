create table if not exists {schema}.cias_abertas
(
	cia_id int not null,
	dt_refer varchar(10),
	versao varchar(30),
   	cd_cvm varchar(10),
	categ_doc varchar(20),
	id_doc varchar(30),
	dt_receb varchar(10),
	link_doc varchar(121),
	constraint fk_cia
        foreign key (cia_id) references {schema}.companies (id)
)