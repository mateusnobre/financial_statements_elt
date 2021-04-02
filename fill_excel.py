import openpyxl as xw
import pyodbc
import sys
import pandas as pd
import os
from dotenv import load_dotenv

# retrieving env variables
load_dotenv()
UID = os.environ.get("UID")
PWD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")
DATABASE = os.environ.get("DATABASE")

def fill_ativo_circ(sheet, info_dict, cnpj, years, start_data_column, latest_data_column, sql_path, cnxn, unused_values):
    quarters = [year + "Q4" for year in years]
    columns = [chr(ord(start_data_column) + i)  for i in range(len(years))]
    columns.append(latest_data_column)
    with open('sql/fill_excel/' + sql_path , 'r') as file:
        sql = file.read()
        sql = sql.format(cnpj, quarters[0], quarters[1], quarters[2], quarters[3])
        df = pd.read_sql(sql, cnxn)
    text = """
    ---------------------------------------------------------------
        Ativo Circulante
    ---------------------------------------------------------------
    """

    unused_values.write(text)
    print(text)
    data_by_quarter = {columns[0]: None,
                        columns[1]: None,
                        columns[2]: None,
                        columns[3]: None,
                        columns[4]: None}

    for quarter, i in zip(quarters, range(len(quarters))):
        data_by_quarter[columns[i]] = df[df['quarter'] == quarter]
        
    print(data_by_quarter[columns[0]][['ds_conta', 'cd_conta', 'vl_conta']])
    for column, data in data_by_quarter.items():
        if data is not None:
            for ds_conta, row_number in info_dict.items():
                value = data[data['ds_conta'] == ds_conta]['vl_conta']
                if not value.empty:
                    data.drop(data['ds_conta'] == ds_conta)
                    sheet[column + row_number] += value.to_numpy()[0]
        unused_values.write(data[['ds_conta', 'cd_conta', 'vl_conta']].to_string())
    unused_values.close()
    return sheet

def fill_ativo_n_circ_rlp(sheet, info_dict, cnpj, years, start_data_column, latest_data_column, sql_path, cnxn, unused_values):
    quarters = [year + "Q4" for year in years]
    columns = [chr(ord(start_data_column) + i)  for i in range(len(years))]
    columns.append(latest_data_column)
    with open('sql/fill_excel/' + sql_path , 'r') as file:
        sql = file.read()
        sql = sql.format(cnpj, quarters[0], quarters[1], quarters[2], quarters[3])
        df = pd.read_sql(sql, cnxn)
    text = """
    ---------------------------------------------------------------
        Ativo Não Circulante
    ---------------------------------------------------------------
    """

    unused_values.write(text)
    print(text)
    data_by_quarter = {columns[0]: None,
                        columns[1]: None,
                        columns[2]: None,
                        columns[3]: None,
                        columns[4]: None}

    for quarter, i in zip(quarters, range(len(quarters))):
        data_by_quarter[columns[i]] = df[df['quarter'] == quarter]
        
    print(data_by_quarter[columns[0]][['ds_conta', 'cd_conta', 'vl_conta']])
    for column, data in data_by_quarter.items():
        if data is not None:
            for ds_conta, row_number in info_dict.items():
                value = data[data['ds_conta'] == ds_conta]['vl_conta']
                if not value.empty:
                    data.drop(data['ds_conta'] == ds_conta)
                    sheet[column + row_number] += value.to_numpy()[0]
        unused_values.write(data[['ds_conta', 'cd_conta', 'vl_conta']].to_string())
    unused_values.close()
    return sheet

def fill_passivo_circ(sheet, info_dict, cnpj, years, start_data_column, latest_data_column, sql_path, cnxn, unused_values):
    quarters = [year + "Q4" for year in years]
    columns = [chr(ord(start_data_column) + i)  for i in range(len(years))]
    columns.append(latest_data_column)
    with open('sql/fill_excel/' + sql_path , 'r') as file:
        sql = file.read()
        sql = sql.format(cnpj, quarters[0], quarters[1], quarters[2], quarters[3])
        df = pd.read_sql(sql, cnxn)
    text = """
    ---------------------------------------------------------------
        Passivo Circulante
    ---------------------------------------------------------------
    """

    unused_values.write(text)
    print(text)
    data_by_quarter = {columns[0]: None,
                        columns[1]: None,
                        columns[2]: None,
                        columns[3]: None,
                        columns[4]: None}

    for quarter, i in zip(quarters, range(len(quarters))):
        data_by_quarter[columns[i]] = df[df['quarter'] == quarter]
        
    print(data_by_quarter[columns[0]][['ds_conta', 'cd_conta', 'vl_conta']])
    for column, data in data_by_quarter.items():
        if data is not None:
            for ds_conta, row_number in info_dict.items():
                value = data[data['ds_conta'] == ds_conta]['vl_conta']
                if not value.empty:
                    data.drop(data['ds_conta'] == ds_conta)
                    sheet[column + row_number] += value.to_numpy()[0]
        unused_values.write(data[['ds_conta', 'cd_conta', 'vl_conta']].to_string())
    unused_values.close()
    return sheet

def fill_passivo_n_circ(sheet, info_dict, cnpj, years, start_data_column, latest_data_column, sql_path, cnxn, unused_values):
    quarters = [year + "Q4" for year in years]
    columns = [chr(ord(start_data_column) + i)  for i in range(len(years))]
    columns.append(latest_data_column)
    with open('sql/fill_excel/' + sql_path , 'r') as file:
        sql = file.read()
        sql = sql.format(cnpj, quarters[0], quarters[1], quarters[2], quarters[3])
        df = pd.read_sql(sql, cnxn)
    text = """
    ---------------------------------------------------------------
        Passivo Não Circulante
    ---------------------------------------------------------------
    """

    unused_values.write(text)
    print(text)
    data_by_quarter = {columns[0]: None,
                        columns[1]: None,
                        columns[2]: None,
                        columns[3]: None,
                        columns[4]: None}

    for quarter, i in zip(quarters, range(len(quarters))):
        data_by_quarter[columns[i]] = df[df['quarter'] == quarter]
        
    print(data_by_quarter[columns[0]][['ds_conta', 'cd_conta', 'vl_conta']])
    for column, data in data_by_quarter.items():
        if data is not None:
            for ds_conta, row_number in info_dict.items():
                value = data[data['ds_conta'] == ds_conta]['vl_conta']
                if not value.empty:
                    data.drop(data['ds_conta'] == ds_conta)
                    sheet[column + row_number] += value.to_numpy()[0]
        unused_values.write(data[['ds_conta', 'cd_conta', 'vl_conta']].to_string())
    unused_values.close()
    return sheet

def fill_patrimonio_liquido(sheet, info_dict, cnpj, years, start_data_column, latest_data_column, sql_path, cnxn, unused_values):
    quarters = [year + "Q4" for year in years]
    columns = [chr(ord(start_data_column) + i)  for i in range(len(years))]
    columns.append(latest_data_column)
    with open('sql/fill_excel/' + sql_path , 'r') as file:
        sql = file.read()
        sql = sql.format(cnpj, quarters[0], quarters[1], quarters[2], quarters[3])
        df = pd.read_sql(sql, cnxn)

    text = """
    ---------------------------------------------------------------
        Patrimônio Líquido
    ---------------------------------------------------------------
    """

    unused_values.write(text)
    print(text)
    data_by_quarter = {columns[0]: None,
                        columns[1]: None,
                        columns[2]: None,
                        columns[3]: None,
                        columns[4]: None}

    for quarter, i in zip(quarters, range(len(quarters))):
        data_by_quarter[columns[i]] = df[df['quarter'] == quarter]
        
    print(data_by_quarter[columns[0]][['ds_conta', 'cd_conta', 'vl_conta']])
    for column, data in data_by_quarter.items():
        if data is not None:
            for ds_conta, row_number in info_dict.items():
                value = data[data['ds_conta'] == ds_conta]['vl_conta']
                if not value.empty:
                    data.drop(data['ds_conta'] == ds_conta)
                    sheet[column + row_number] += value.to_numpy()[0]
        unused_values.write(data[['ds_conta', 'cd_conta', 'vl_conta']].to_string())
    unused_values.close()
    return sheet

def fill_demonstracao_resultado(sheet, info_dict, cnpj, years, start_data_column, latest_data_column, sql_path, cnxn, unused_values):
    quarters = ['CUM_' + year + "Q4" for year in years]
    columns = [chr(ord(start_data_column) + i)  for i in range(len(years))]
    columns.append(latest_data_column)
    with open('sql/fill_excel/' + sql_path , 'r') as file:
        sql = file.read()
        sql = sql.format(cnpj, quarters[0], quarters[1], quarters[2], quarters[3])
        df = pd.read_sql(sql, cnxn)
    text = """
    ---------------------------------------------------------------
        Demonstração de Resultado do Exercício
    ---------------------------------------------------------------
    """

    unused_values.write(text)
    print(text)
    data_by_quarter = {columns[0]: None,
                        columns[1]: None,
                        columns[2]: None,
                        columns[3]: None,
                        columns[4]: None}

    for quarter, i in zip(quarters, range(len(quarters))):
        data_by_quarter[columns[i]] = df[df['quarter'] == quarter]
        
    print(data_by_quarter[columns[0]][['ds_conta', 'cd_conta', 'vl_conta']])
    for column, data in data_by_quarter.items():
        if data is not None:
            for ds_conta, row_number in info_dict.items():
                value = data[data['ds_conta'] == ds_conta]['vl_conta']
                if not value.empty:
                    data.drop(data['ds_conta'] == ds_conta)
                    sheet[column + row_number] += value.to_numpy()[0]
        unused_values.write(data[['ds_conta', 'cd_conta', 'vl_conta']].to_string())
    unused_values.close()
    return sheet

def main():
    # print command line arguments
    cnpj = sys.argv[1]
    connection_string = "Driver={ODBC Driver 17 for SQL Server};"+"Server={0};".format(SERVER)+"Database={0};".format(DATABASE)+"UID={0};".format(UID)+"PWD={0};".format(PWD)
    cnxn = pyodbc.connect(connection_string)
    years = ['2016', '2017', '2018', '2019']
    wb = xw.load_workbook('Spread - Entrada.xlsm') 
    sht = wb['Entrada']
    latest_data_column = 'L'
    start_data_column = 'D'
    rows_ativo_circ = {
        "Caixa e Equivalentes de Caixa" : "30",
        "Aplicações Financeiras" : "29",
        "Contas a Receber" : "32",
        "Estoques" : "36",
        "Adiantamento a Fornecedores" : "39",
        "Tributos a Recuperar" : "40",
        "Despesas Antecipadas" : "41",
        "Ativos de Operações Descontinuadas" : "44",
        "Dividendos a Receber" : "45",
        "Ativos Biológicos" : "53",
        "Partes Relacionadas" : "48",
        "Outros Ativos Circulantes" : "53"
    }

    rows_ativo_n_circ_rlp = {
        "Investimentos" : "77",
        "Intangível" : "86",
        "Imobilizado" : "80",
        "adto a fornecedores lp" : "61",
        "impostos a recuperar lp" : "62",
        "ativos ncg lp" : "63",
        "ativo não operacional lp" : "65",
        "ir e cs diferidos a recuperar" : "66",
        "imposto de renda e crédito social a recuperar" : "67",
        "coligadas" : "68",
        "depósitos judiciais" : "70",
        "direito de uso" : "46",
        "outros ativos" : "47"
    }
    rows_passivo_circ = {
        "Obrigações Sociais e Trabalhistas" : "106",
        "Fornecedores Nacionais" : "103",
        "Fornecedores Estrangeiros" : "104",
        "Obrigações Fiscais Federais" : "107",
        "Obrigações Fiscais Estaduais" : "108",
        "Obrigações Fiscais Municipais" : "108",
        "Em Moeda Nacional" : "97",
        "Em Moeda Estrangeira" : "99",
        "Debêntures" : "98",
        "Financiamento por Arrendamento Financeiro" : "119",
        "Outras Obrigações" : "121"
    }
    rows_passivo_n_circ = {
        "Em Moeda Nacional" : "56",
        "Em Moeda Estrangeira" : "58",
        "Debêntures" : "60",
        "Financiamento por Arrendamento Financeiro" : "61",
        "Provisões": '138',
        "Provisões Fiscais": '137'
    }
    rows_patrimonio_liquido = {
        "Capital Social Realizado" : "146",
        "Reservas de Capital": "147",
        "Reservas de Reavaliação": "148",
        "Reservas de Lucro": "149",
        "Ajustes de Avaliação Patrimonial": '148',
        "Ajustes Acumulados de Conversão": '148',
        "Lucros/Prejuízos Acumulados": '150',
    }
    rows_demonstracao_resultado = {
        "Receita de Venda de Bens e/ou Serviços" : "158",
        "Custo dos Bens e/ou Serviços Vendidos" : "173",
        "Despesas Gerais e Administrativas" : "185",
        "Corrente" : "209",
        "Diferido" : "210",
        "Resultado de Equivalência Patrimonial" : "207",
        "Despesas com Vendas" : "189",
        "Outras Receitas Operacionais" : "190",
        "Outras Despesas Operacionais" : "192",
        "Receitas Financeiras" : "195",
        "Despesas Financeiras" : "197",
        "Resultado Líquido das Operações Continuadas": "212"
    }

    unused_values = open("unused_values.txt", "a")

    sht = fill_demonstracao_resultado(sht, rows_demonstracao_resultado, cnpj, years, start_data_column, latest_data_column, "select_demonstracao_resultado.sql", cnxn, unused_values)
    print(sht)
    wb.save(filename = 'Spread - Entrada.xlsm')
    
    sht = fill_ativo_circ(sht, rows_ativo_circ, cnpj, years, start_data_column, latest_data_column, "select_ativo_circ.sql", cnxn, unused_values)
    print(sht)
    wb.save(filename = 'Spread - Entrada.xlsm')

    sht = fill_ativo_n_circ_rlp(sht, rows_ativo_n_circ_rlp, cnpj, years, start_data_column, latest_data_column, "select_ativo_n_circ.sql", cnxn, unused_values)
    print(sht)
    wb.save(filename = 'Spread - Entrada.xlsm')
    sht = fill_passivo_circ(sht, rows_passivo_circ, cnpj, years, start_data_column, latest_data_column, "select_passivo_circ.sql", cnxn, unused_values)
    print(sht)
    wb.save(filename = 'Spread - Entrada.xlsm')
    sht = fill_passivo_n_circ(sht, rows_passivo_n_circ, cnpj, years, start_data_column, latest_data_column, "select_passivo_n_circ.sql", cnxn, unused_values)
    print(sht)
    wb.save(filename = 'Spread - Entrada.xlsm')
    sht = fill_patrimonio_liquido(sht, rows_patrimonio_liquido, cnpj, years, start_data_column, latest_data_column, "select_patrimonio_liquido.sql", cnxn, unused_values)
    print(sht)
    wb.save(filename = 'Spread - Entrada.xlsm')

    unused_values.close()        
if __name__ == "__main__":
    main()