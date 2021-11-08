select
   	cnpj_cia,
	dt_refer,
	versao,
	denom_cia,
   	cd_cvm,
	categ_doc,
	id_doc,
	dt_receb,
	link_doc
from (
    select *
    from {schema}.itr_cia_aberta
    union all
    select *
    from {schema}.dfp_cia_aberta
 ) df