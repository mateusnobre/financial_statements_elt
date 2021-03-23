
import luigi
import logging
import pyodbc
import pandas as pd
import csv
import requests
import zipfile
from io import BytesIO
import os

# retrieving env variables

UID = os.getenv("UID")
PWD = os.getenv("PWD")

class DownloadCSVs(luigi.Task):
    def __init__(self):            
        super().__init__()
        self.years = None
    def requires(self):
        return []
    def output(self):
        return None
    def run(self):
        self.years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        
        for year in self.years:
            if not os.path.isfile('data/itr_cia_aberta_' + year + '.csv'):
                response_itr = requests.get('http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_' + year +'.zip', stream = True)
                if response_itr.ok:
                    z = zipfile.ZipFile(BytesIO(response_itr.content))
                    print('Succesfully downloaded {0} itr data'.format(year))
                    z.extractall('data')
                    print('Finished extracting itr data from {0}'.format(year))
            if not os.path.isfile('data/dfp_cia_aberta_' + year + '.csv'):    
                response_dfp = requests.get('http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_' + year + '.zip', stream = True)
                if response_dfp.ok:
                    z = zipfile.ZipFile(BytesIO(response_dfp.content))
                    print('Succesfully downloaded {0} dfp data'.format(year))
                    z.extractall('data')
                    print('Finished extracting dfp data from {0}'.format(year))

class FromCSVToSQLServer(luigi.Task):
    
    def __init__(self,
                stg_schema = 'staging',
                dwh_schema = 'financial_statements',
                pg_table_pks = 'id'):            
        super().__init__()
        self.stg_schema = stg_schema
        self.dwh_schema = dwh_schema
        self.table_names = None
        self.years = None
    def requires(self):
        return []#[DownloadCSVs()]
    def output(self):
        return luigi.LocalTarget([self.table_names, self.years])
    def run(self):
        
        file_prefixes = ["itr_cia_aberta", 'dfp_cia_aberta']
        self.years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        table_suffixes = ['DFC_MI_ind', "DMPL_con", "DMPL_ind"]#['', 'BPA_con', 'BPA_ind', 'BPP_con', 'BPP_ind', 'DFC_MD_con', 'DFC_MD_ind', 'DFC_MI_con', 'DFC_MI_ind', "DMPL_con", "DMPL_ind", "DRE_con", "DRE_ind", "DVA_con", "DVA_ind"]
        self.table_names = [file_prefix + '_' + table_suffix for table_suffix in table_suffixes for file_prefix in file_prefixes]
        
        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=localhost, 1433;"
                      "Database=master;"
                      "UID=SA;"
                      "PWD=<YourStrong@Passw0rd>;")

        for table_name in self.table_names:
                for year in self.years:
                    logging.info("Transferring Postgres query results into Data Warehouse database.")
                    with open ('data/' + table_name + '_' +year + '.csv', 'r', encoding= 'unicode_escape') as f:
                        reader = csv.reader(f, delimiter = ';')
                        columns = next(reader)
                        columns.append('ano')
                        query = """
                                insert into {0}.{1}({2}) values ({3})"""
                        query = query.format(self.dwh_schema, table_name, ','.join(columns), ','.join('?' * len(columns)))
                        cursor = cnxn.cursor()
                        logging.info("Inserting rows into Postgres with this query:")
                        logging.info(query)
                        for data in reader:
                            data.append(year)
                            cursor.execute(query, data) # accumulate rows on cursor before inserting
                        cursor.commit()
                        print("Done loading data from {1} into {0}.".format(table_name, year))
    
class ProcessData(luigi.Task):
    def __init__(self,
                stg_schema = 'staging',
                dwh_schema = 'dwh',
                pg_table_pks = 'id'):            
        super().__init__()
        self.stg_schema = stg_schema
        self.dwh_schema = dwh_schema
        self.table_names = None
        self.years = None
    
    def requires(self):
        return []#[FromCSVToSQLServer()]

    def output(self):
        return None

    def run(self):
        #table_names = self.input()[0]

        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=localhost, 1433;"
                      "Database=master;"
                      "UID=SA;"
                      "PWD=<YourStrong@Passw0rd>;")

        sql_paths = ['select_demonstracao_resultado_ind.sql', 'select_demonstracao_resultado_con.sql', 'select_balanco_ativo_ind.sql', 'select_balanco_ativo_con.sql', 'select_balanco_passivo_ind.sql', 'select_balanco_passivo_con.sql']
        self.table_names = ['demonstracao_resultado_ind', 'demonstracao_resultado_con', 'balanco_ativo_ind', 'balanco_ativo_con', 'balanco_passivo_ind', 'balanco_passivo_con']
        cursor = cnxn.cursor()

        for table_name, sql_path in zip(self.table_names, sql_paths):
                with open('sql/' + sql_path , 'r') as file:
                    sql = file.read()
                    data = pd.read_sql(sql = sql, con = cnxn)
                    if table_name in ['demonstracao_resultado_ind', 'demonstracao_resultado_con']:
                        columns = """cnpj_cia,
                                    denom_cia,
                                    ds_conta,
                                    cd_conta,
                                    vl_conta,
                                    quarter,
                                    dt_ini_exerc,
                                    dt_fim_exerc"""
                    else:
                        columns = """cnpj_cia,
                                    denom_cia,
                                    ds_conta,
                                    cd_conta
                                    vl_conta,
                                    quarter,
                                    dt_fim_exerc,
                                    dt_refer"""
                    table = self.dwh_schema + '.' + table_name
                    print("Starting processing {0} data".format(table))
                    cursor.execute("truncate table {0}".format(table))
                    cursor.executemany("""                
                    insert into {0} values (?, ?, ?, ?, ?, ?, ?, ?)""".format(table),
                     data.values.tolist())
                    print('Done processing data into {0}.{1}'.format(self.dwh_schema, table_name))
                    cursor.commit()

class DeleteCSVs(luigi.Task):
    def __init__(self):            
        super().__init__()
    
    def requires(self):
        return []#[ProcessData()]

    def output(self):
        return None

    def run(self):
        directory = "./data"
        files_in_directory = os.listdir(directory)
        filtered_files = [file for file in files_in_directory if file.endswith(".csv")]
        for file in filtered_files:
        	path_to_file = os.path.join(directory, file)
        	os.remove(path_to_file)


if __name__ == '__main__':
    luigi.run()