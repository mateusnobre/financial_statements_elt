with aux as (
select cnpj_cia,
       denom_cia,
       ano,
       dt_refer,
       dt_ini_exerc,
       DT_FIM_EXERC,
       (case when (ano = 2011 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2011Q1'
            when (ano = 2011 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2011Q2'
            when (ano = 2011 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2011Q3'
            when (ano = 2011 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2011Q4'
            when (ano = 2011 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2011Q2'
            when (ano = 2011 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2011Q3'
            when (ano = 2011 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2011Q4'
             when (ano = 2012 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2012Q1'
            when (ano = 2012 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2012Q2'
            when (ano = 2012 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2012Q3'
            when (ano = 2012 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2012Q4'
            when (ano = 2012 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2012Q2'
            when (ano = 2012 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2012Q3'
            when (ano = 2012 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2012Q4'
             when (ano = 2013 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2013Q1'
            when (ano = 2013 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2013Q2'
            when (ano = 2013 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2013Q3'
            when (ano = 2013 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2013Q4'
            when (ano = 2013 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2013Q2'
            when (ano = 2013 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2013Q3'
            when (ano = 2013 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2013Q4'
             when (ano = 2014 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2014Q1'
            when (ano = 2014 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2014Q2'
            when (ano = 2014 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2014Q3'
            when (ano = 2014 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2014Q4'
            when (ano = 2014 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2014Q2'
            when (ano = 2014 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2014Q3'
            when (ano = 2014 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2014Q4'
             when (ano = 2015 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2015Q1'
            when (ano = 2015 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2015Q2'
            when (ano = 2015 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2015Q3'
            when (ano = 2015 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2015Q4'
            when (ano = 2015 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2015Q2'
            when (ano = 2015 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2015Q3'
            when (ano = 2015 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2015Q4'
             when (ano = 2016 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2016Q1'
            when (ano = 2016 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2016Q2'
            when (ano = 2016 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2016Q3'
            when (ano = 2016 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2016Q4'
            when (ano = 2016 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2016Q2'
            when (ano = 2016 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2016Q3'
            when (ano = 2016 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2016Q4'
             when (ano = 2017 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2017Q1'
            when (ano = 2017 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2017Q2'
            when (ano = 2017 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2017Q3'
            when (ano = 2017 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2017Q4'
            when (ano = 2017 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2017Q2'
            when (ano = 2017 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2017Q3'
            when (ano = 2017 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2017Q4'
             when (ano = 2018 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2018Q1'
            when (ano = 2018 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2018Q2'
            when (ano = 2018 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2018Q3'
            when (ano = 2018 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2018Q4'
            when (ano = 2018 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2018Q2'
            when (ano = 2018 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2018Q3'
            when (ano = 2018 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2018Q4'
             when (ano = 2019 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2019Q1'
            when (ano = 2019 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2019Q2'
            when (ano = 2019 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2019Q3'
            when (ano = 2019 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2019Q4'
            when (ano = 2019 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2019Q2'
            when (ano = 2019 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2019Q3'
            when (ano = 2019 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2019Q4'
             when (ano = 2020 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2020Q1'
            when (ano = 2020 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2020Q2'
            when (ano = 2020 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2020Q3'
            when (ano = 2020 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2020Q4'
            when (ano = 2020 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2020Q2'
            when (ano = 2020 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2020Q3'
            when (ano = 2020 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2020Q4'
             when (ano = 2021 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2021Q1'
            when (ano = 2021 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2021Q2'
            when (ano = 2021 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2021Q3'
            when (ano = 2021 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2021Q4'
            when (ano = 2021 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2021Q2'
            when (ano = 2021 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2021Q3'
            when (ano = 2021 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2021Q4'
             when (ano = 2022 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (3,4))       then '2022Q1'
            when (ano = 2022 AND datepart(month , DT_INI_EXERC) in (3,4) AND datepart(month , DT_FIM_EXERC) in (6,7))   then '2022Q2'
            when (ano = 2022 AND datepart(month , DT_INI_EXERC) in (6,7) AND datepart(month , DT_FIM_EXERC) in (9,10))  then '2022Q3'
            when (ano = 2022 AND datepart(month , DT_INI_EXERC) in (9,10) AND datepart(month , DT_FIM_EXERC) = 12)      then '2022Q4'
            when (ano = 2022 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (6,7))        then 'CUM_2022Q2'
            when (ano = 2022 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) in (9,10))       then 'CUM_2022Q3'
            when (ano = 2022 AND datepart(month , DT_INI_EXERC) = 1 AND datepart(month , DT_FIM_EXERC) = 12)            then 'CUM_2022Q4'
             else null end) quarter,
       (case when escala_moeda = 'MIL' then vl_conta * 1000
           when escala_moeda = 'UNIDADE' then vl_conta
           else 0 end) vl_conta,
       ds_conta,
       cd_conta
       --replace(substring(cd_conta, 1, 2), '.', '') as level_1,
       --substring(cd_conta, 3, 2) as level_2,
       --substring(cd_conta, 6, 2) as level_3,
       --substring(cd_conta, 9, 2) as level_4,
       --substring(cd_conta, 12, 2) as level_5
from (
    select *
    from financial_statements.itr_cia_aberta_DFC_MI_ind
    union all
    select *
    from financial_statements.dfp_cia_aberta_DFC_MI_ind
 ) df
where df.ordem_exerc = 'ÚLTIMO')

select cnpj_cia,
    replace(denom_cia, '.', '') denom_cia,
    ds_conta,
    cd_conta,
    vl_conta,
    quarter,
    dt_ini_exerc,
    DT_FIM_EXERC
from aux
order by cnpj_cia asc, DT_FIM_EXERC asc, CD_CONTA asc