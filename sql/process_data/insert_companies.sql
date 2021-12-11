insert into {dw_schema}.companies (denom, cnpj)
    (
        select distinct denom_cia, cnpj_cia
        from {st_schema}.dfp_cia_aberta
        union
        select distinct denom_cia, cnpj_cia
        from {st_schema}.itr_cia_aberta
    )
        order by denom_cia;