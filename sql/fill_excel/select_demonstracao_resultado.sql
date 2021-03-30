select *
from dwh.demonstracao_resultado_ind
where cnpj_cia = '{0}'
    and quarter in ('{1}', '{2}', '{3}', '{4}')