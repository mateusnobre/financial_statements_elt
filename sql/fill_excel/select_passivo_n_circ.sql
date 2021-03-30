select *
from dwh.balanco_passivo_ind
where cnpj_cia = '{0}'
    and quarter in ('{1}', '{2}', '{3}', '{4}')
    and cd_conta like '2.02.%'