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
    from financial_statements.itr_cia_aberta
    union all
    select *
    from financial_statements.dfp_cia_aberta
 ) df