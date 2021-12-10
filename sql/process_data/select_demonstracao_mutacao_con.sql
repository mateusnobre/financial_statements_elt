with aux as (
    select cnpj_cia,
           ano::varchar(4),
           (case
                when date_part('month', to_date(DT_FIM_EXERC, 'YYYY-MM-DD')) in (3, 4) then ano || 'Q1'
                when date_part('month', to_date(DT_FIM_EXERC, 'YYYY-MM-DD')) in (6, 7) then ano || 'Q2'
                when date_part('month', to_date(DT_FIM_EXERC, 'YYYY-MM-DD')) in (9, 10) then ano || 'Q3'
                when date_part('month', to_date(DT_FIM_EXERC, 'YYYY-MM-DD')) = 12 then ano || 'Q4'
               end)                               quarter,
           (case
                when escala_moeda = 'MIL' then vl_conta * 1000
                when escala_moeda = 'UNIDADE' then vl_conta
                else 0 end)                       vl_conta,
           ds_conta,
           cd_conta,
           coluna_df
    from (
             select *
             from {st_schema}.itr_cia_aberta_DMPL_con
             union all
             select *
             from {st_schema}.dfp_cia_aberta_DMPL_con
         ) df
    where df.ordem_exerc = 'ÚLTIMO')

select distinct companies.id as cia_id,
       ds_conta,
       cd_conta,
       vl_conta,
       quarter,
       coluna_df
from aux
         join {dw_schema}.companies on aux.cnpj_cia = {dw_schema}.companies.cnpj
order by cia_id, quarter, CD_CONTA