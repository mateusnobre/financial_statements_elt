with aux as (
select cnpj_cia,
       denom_cia,
       ano,
       dt_refer,
       (case when datepart(month , dt_refer) < 6 then 1
           when datepart(month , dt_refer) < 9 then 2
           when datepart(month , dt_refer) < 12 then 3 else 4 end) quarter,
       (case when escala_moeda = 'MIL' then vl_conta * 1000
           when escala_moeda = 'UNIDADE' then vl_conta
           else 0 end) vl_conta,
       ds_conta,
       cd_conta,
       replace(substring(cd_conta, 1, 2), '.', '') as level_1,
       substring(cd_conta, 3, 2) as level_2,
       substring(cd_conta, 6, 2) as level_3,
       substring(cd_conta, 9, 2) as level_4,
       substring(cd_conta, 12, 2) as level_5
from (select *
    from financial_statements.itr_cia_aberta_BPA_ind
    union all
    select *
    from financial_statements.dfp_cia_aberta_BPA_ind
 )cia_aberta_BPA_ind
where cia_aberta_BPA_ind.ordem_exerc = 'ÚLTIMO')

select replace(replace(replace(cnpj_cia, '.', ''), '/',''), '-', '') cnpj_cia,
    replace(denom_cia, '.', '') denom_cia,
    ds_conta,
    cd_conta,
    sum(case when ano = 2011 and quarter = 1 then vl_conta else 0 end) valor_2011_q1,
    sum(case when ano = 2011 and quarter = 2 then vl_conta else 0 end) valor_2011_q2,
    sum(case when ano = 2011 and quarter = 3 then vl_conta else 0 end) valor_2011_q3,
    sum(case when ano = 2011 and quarter = 4 then vl_conta else 0 end) valor_2011_q4,
    sum(case when ano = 2012 and quarter = 1 then vl_conta else 0 end) valor_2012_q1,
    sum(case when ano = 2012 and quarter = 2 then vl_conta else 0 end) valor_2012_q2,
    sum(case when ano = 2012 and quarter = 3 then vl_conta else 0 end) valor_2012_q3,
    sum(case when ano = 2012 and quarter = 4 then vl_conta else 0 end) valor_2012_q4,
    sum(case when ano = 2013 and quarter = 1 then vl_conta else 0 end) valor_2013_q1,
    sum(case when ano = 2013 and quarter = 2 then vl_conta else 0 end) valor_2013_q2,
    sum(case when ano = 2013 and quarter = 3 then vl_conta else 0 end) valor_2013_q3,
    sum(case when ano = 2013 and quarter = 4 then vl_conta else 0 end) valor_2013_q4,
    sum(case when ano = 2014 and quarter = 1 then vl_conta else 0 end) valor_2014_q1,
    sum(case when ano = 2014 and quarter = 2 then vl_conta else 0 end) valor_2014_q2,
    sum(case when ano = 2014 and quarter = 3 then vl_conta else 0 end) valor_2014_q3,
    sum(case when ano = 2014 and quarter = 4 then vl_conta else 0 end) valor_2014_q4,
    sum(case when ano = 2015 and quarter = 1 then vl_conta else 0 end) valor_2015_q1,
    sum(case when ano = 2015 and quarter = 2 then vl_conta else 0 end) valor_2015_q2,
    sum(case when ano = 2015 and quarter = 3 then vl_conta else 0 end) valor_2015_q3,
    sum(case when ano = 2015 and quarter = 4 then vl_conta else 0 end) valor_2015_q4,
    sum(case when ano = 2016 and quarter = 1 then vl_conta else 0 end) valor_2016_q1,
    sum(case when ano = 2016 and quarter = 2 then vl_conta else 0 end) valor_2016_q2,
    sum(case when ano = 2016 and quarter = 3 then vl_conta else 0 end) valor_2016_q3,
    sum(case when ano = 2016 and quarter = 4 then vl_conta else 0 end) valor_2016_q4,
    sum(case when ano = 2017 and quarter = 1 then vl_conta else 0 end) valor_2017_q1,
    sum(case when ano = 2017 and quarter = 2 then vl_conta else 0 end) valor_2017_q2,
    sum(case when ano = 2017 and quarter = 3 then vl_conta else 0 end) valor_2017_q3,
    sum(case when ano = 2017 and quarter = 4 then vl_conta else 0 end) valor_2017_q4,
    sum(case when ano = 2018 and quarter = 1 then vl_conta else 0 end) valor_2018_q1,
    sum(case when ano = 2018 and quarter = 2 then vl_conta else 0 end) valor_2018_q2,
    sum(case when ano = 2018 and quarter = 3 then vl_conta else 0 end) valor_2018_q3,
    sum(case when ano = 2018 and quarter = 4 then vl_conta else 0 end) valor_2018_q4,
    sum(case when ano = 2019 and quarter = 1 then vl_conta else 0 end) valor_2019_q1,
    sum(case when ano = 2019 and quarter = 2 then vl_conta else 0 end) valor_2019_q2,
    sum(case when ano = 2019 and quarter = 3 then vl_conta else 0 end) valor_2019_q3,
    sum(case when ano = 2019 and quarter = 4 then vl_conta else 0 end) valor_2019_q4,
    sum(case when ano = 2020 and quarter = 1 then vl_conta else 0 end) valor_2020_q1,
    sum(case when ano = 2020 and quarter = 2 then vl_conta else 0 end) valor_2020_q2,
    sum(case when ano = 2020 and quarter = 3 then vl_conta else 0 end) valor_2020_q3,
    sum(case when ano = 2020 and quarter = 4 then vl_conta else 0 end) valor_2020_q4,
    sum(case when ano = 2021 and quarter = 1 then vl_conta else 0 end) valor_2021_q1,
    sum(case when ano = 2021 and quarter = 2 then vl_conta else 0 end) valor_2021_q2,
    sum(case when ano = 2021 and quarter = 3 then vl_conta else 0 end) valor_2021_q3,
    sum(case when ano = 2021 and quarter = 4 then vl_conta else 0 end) valor_2021_q4,
    sum(case when ano = 2022 and quarter = 1 then vl_conta else 0 end) valor_2022_q1,
    sum(case when ano = 2022 and quarter = 2 then vl_conta else 0 end) valor_2022_q2,
    sum(case when ano = 2022 and quarter = 3 then vl_conta else 0 end) valor_2022_q3,
    sum(case when ano = 2022 and quarter = 4 then vl_conta else 0 end) valor_2022_q4
from aux
where level_4 = ''
group by cnpj_cia, denom_cia, ds_conta, cd_conta
