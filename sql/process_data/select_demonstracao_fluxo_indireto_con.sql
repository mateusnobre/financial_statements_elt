with aux as (
    select cnpj_cia,
           ano::varchar(4),
           dt_refer,
           dt_ini_exerc,
           to_date(DT_FIM_EXERC, 'YYYY-MM-DD') as DT_FIM_EXERC,
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
           cd_conta
    from (
             select *
             from {st_schema}.itr_cia_aberta_DFC_MI_con
             union all
             select *
             from {st_schema}.dfp_cia_aberta_DFC_MI_con
         ) df
    where df.ordem_exerc = 'ÚLTIMO')

select distinct companies.id as cia_id,
       ds_conta,
       cd_conta,
       vl_conta,
       quarter,
       dt_ini_exerc,
       DT_FIM_EXERC
from aux
         join {dw_schema}.companies on aux.cnpj_cia = {dw_schema}.companies.cnpj
order by cia_id, DT_FIM_EXERC, CD_CONTA