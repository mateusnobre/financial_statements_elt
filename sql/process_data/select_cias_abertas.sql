select distinct
   	companies.id as cia_id,
	dt_refer,
	versao,
   	cd_cvm,
	categ_doc,
	id_doc,
	dt_receb,
	link_doc
from (
    select *
    from {st_schema}.itr_cia_aberta
    union all
    select *
    from {st_schema}.dfp_cia_aberta
 ) df
	join {dw_schema}.companies on df.cnpj_cia = {dw_schema}.companies.cnpj