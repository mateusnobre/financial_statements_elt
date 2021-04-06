
import luigi
import pyodbc
import pandas as pd
import csv
import requests
import zipfile
import time
from io import BytesIO
import os
from dotenv import load_dotenv

# retrieving env variables
load_dotenv()
UID = os.environ.get("UID")
PWD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")
DATABASE = os.environ.get("DATABASE")

# defining the year to extract and process data from
YEARS = ['2011', '2012', '2013', '2014', '2015','2016', '2017', '2018', '2019''2020','2021', '2022']

# defining if we want both quartely and yearly data
FILE_PREFIXES = ['itr_cia_aberta', 'dfp_cia_aberta']

# defining the tables that we want to extract and process data from
TABLE_SUFFIXES = ["DMPL_con",
                "DMPL_ind",
                'DRE_ind',
                "DRE_con",
                'BPA_con',
                'BPA_ind',
                'BPP_con',
                'BPP_ind',
                'DFC_MD_con',
                'DFC_MD_ind',
                'DFC_MI_con',
                'DFC_MI_ind',
                "DVA_con",
                "DVA_ind"]
 
class DownloadCSVs(luigi.Task):
    def __init__(self):            
        super().__init__()
        self.years = None
        self.task_complete = False
    def requires(self):
        return []
    def output(self):
        return None
    def run(self):
        self.years = YEARS
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
        self.task_complete = True
    def complete(self):
            # Make sure you return false when you want the task to run.
            # And true when complete

            return  self.task_complete

class FromCSVToSQLServer(luigi.Task):
    
    def __init__(self,
                stg_schema = 'staging',
                dwh_schema = 'financial_statements',
                pg_table_pks = 'id'):            
        super().__init__()
        self.stg_schema = stg_schema
        self.dwh_schema = dwh_schema
        self.table_names = None
        self.years = YEARS
        self.task_complete = False 
    def requires(self):
        return [DownloadCSVs()]
    def output(self):
        return None
    def run(self):
        
        file_prefixes = FILE_PREFIXES 
        table_suffixes = TABLE_SUFFIXES
        self.table_names = [file_prefix + '_' + table_suffix for table_suffix in table_suffixes for file_prefix in file_prefixes]
        for file_prefix in file_prefixes:
            self.table_names.append(file_prefix)
        connection_string = "Driver={ODBC Driver 17 for SQL Server};"+"Server={0};".format(SERVER)+"Database={0};".format(DATABASE)+"UID={0};".format(UID)+"PWD={0};".format(PWD)
        cnxn = pyodbc.connect(connection_string)
        tables_time = dict()
        start = time.time()
        years_time = dict()
        for year in self.years:
            year_start = time.time()
            for table_name in self.table_names:
                i=0
                table_start = time.time()
                print("""
                ----------------------------------------------------------------
                """)
                with open ('data/' + table_name + '_' +year + '.csv', 'r', encoding= 'unicode_escape') as f:
                    reader = csv.reader(f, delimiter = ';')
                    columns = next(reader)
                    columns.append('ano')
                    delete_query = """
                            delete from {0}.{1} where ano = {2}""".format(self.dwh_schema, table_name, int(year))
                    insert_query  = """insert into {0}.{1}({2}) values ({3})"""
                    insert_query = insert_query.format(self.dwh_schema, table_name, ','.join(columns), ','.join('?' * len(columns)))
                    cursor = cnxn.cursor()
                    print("Deleting data from {0} already in the {1} table.".format(year, table_name))
                    cursor.execute(delete_query)
                    print("Start loading data from {1} into {0}".format(year, table_name))
                    for data in reader:
                        try:
                            data.append(year)
                            cursor.execute(insert_query, data) # accumulate rows on cursor before inserting
                            i = i+1
                        except:
                            i = i+1
                            print("Couldn't process line {0} of {1}_{2}".format(i, table_name, year))

                    cursor.commit()
                    table_end = time.time()
                    table_delta_minutes = round(((table_end - table_start)/60),2)
                    tables_time[table_name] = 0 
                    tables_time[table_name] += table_delta_minutes 
                    print("Done loading data from {1} into {0} in {2} minutes.".format(year, table_name, table_delta_minutes))
            year_end = time.time()
            delta_year_hours = round(((year_end-year_start)/3600), 2)
            years_time[year] = delta_year_hours
            directory = "./data"
            files_in_directory = os.listdir(directory)
            filtered_files = [file for file in files_in_directory if file.endswith(year+".csv")]
            for file in filtered_files:
                try:
            	    path_to_file = os.path.join(directory, file)
            	    os.remove(path_to_file)
                except:
                    print("Cannot delete {0}, check if the file exist".format(file))
            print("Year {0} fully processed in {1} hours".format(year,delta_year_hours))
            print("""
            ----------------------------------------------------------------
            ----------------------------------------------------------------
            ----------------------------------------------------------------
            """)
        all_files_csv = [file for file in files_in_directory if file.endswith(".csv")]
        for file in all_files_csv:
        	path_to_file = os.path.join(directory, file)
        	os.remove(path_to_file)
        end = time.time()
        print(years_time)
        print(tables_time)
        print("Finished task in {0} hours".format(round((end-start)/3600),2))
        self.task_complete = True
    def complete(self):
            # Make sure you return false when you want the task to run.
            # And true when complete

            return  self.task_complete
    
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
        self.task_complete = False 
    
    def requires(self):
        return [FromCSVToSQLServer()]

    def output(self):
        return None

    def run(self):

        connection_string = "Driver={ODBC Driver 17 for SQL Server};"+"Server={0};".format(SERVER)+"Database={0};".format(DATABASE)+"UID={0};".format(UID)+"PWD={0};".format(PWD)
        cnxn = pyodbc.connect(connection_string)
        # defining the sql files that will process each of the tables
        # be aware that the sql_paths order MUST MATCH the table names order
        sql_paths = ['select_demonstracao_resultado_ind.sql',
                    'select_demonstracao_resultado_con.sql',
                    'select_balanco_ativo_ind.sql',
                    'select_balanco_ativo_con.sql',
                    'select_balanco_passivo_ind.sql',
                    'select_balanco_passivo_con.sql',
                    'select_cias_abertas.sql',
                    'select_demonstracao_fluxo_direto_con.sql',
                    'select_demonstracao_fluxo_direto_ind.sql',
                    'select_demonstracao_fluxo_indireto_con.sql',
                    'select_demonstracao_fluxo_indireto_ind.sql',
                    'select_demonstracao_valor_adicionado_con.sql',
                    'select_demonstracao_valor_adicionado_ind.sql',
                    'select_demonstracao_mutacao_con.sql',
                    'select_demonstracao_mutacao_ind.sql'
                    ]
        self.table_names = ['demonstracao_resultado_ind',
                    'demonstracao_resultado_con',
                    'balanco_ativo_ind',
                    'balanco_ativo_con',
                    'balanco_passivo_ind',
                    'balanco_passivo_con',
                    'cias_abertas',
                    'demonstracao_fluxo_direto_con',
                    'demonstracao_fluxo_direto_ind',
                    'demonstracao_fluxo_indireto_con',
                    'demonstracao_fluxo_indireto_ind',
                    'demonstracao_valor_adicionado_con',
                    'demonstracao_valor_adicionado_ind',
                    'demonstracao_mutacao_con',
                    'demonstracao_mutacao_ind'                    
                    ]
        
        cursor = cnxn.cursor()
        start_time = time.time()
        tables_time = dict()
        for table_name, sql_path in zip(self.table_names, sql_paths):
            with open('sql/' + sql_path , 'r') as file:
                table_start = time.time()
                sql = file.read()
                data = pd.read_sql(sql = sql, con = cnxn)
                if table_name in ['demonstracao_resultado_ind',
                    'demonstracao_resultado_con',
                    'demonstracao_fluxo_direto_con',
                    'demonstracao_fluxo_direto_ind',
                    'demonstracao_fluxo_indireto_con',
                    'demonstracao_fluxo_indireto_ind',
                    'demonstracao_valor_adicionado_con',
                    'demonstracao_valor_adicionado_ind']:
                    columns = """cnpj_cia,
                                denom_cia,
                                ds_conta,
                                cd_conta,
                                vl_conta,
                                quarter,
                                dt_ini_exerc,
                                dt_fim_exerc"""
                elif table_name in ['demonstracao_mutacao_ind', 'demonstracao_mutacao_con']:
                    columns = """cnpj_cia,
                        denom_cia,
                        ds_conta,
                        cd_conta,
                        vl_conta,
                        quarter,
                        dt_ini_exerc,
                        dt_fim_exerc,
                        coluna_df"""
                elif table_name in ['cias_abertas']:
                    columns = """cnpj_cia,
	                    dt_refer,
	                    versao,
	                    denom_cia,
   	                    cd_cvm,
	                    categ_doc,
	                    id_doc,
	                    dt_receb,
	                    link_doc"""
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
                if table_name in ['cias_abertas']:
                    cursor.executemany("""                
                    insert into {0} values ({1})""".format(table, ','.join('?' * 9)), data.values.tolist())
                else:
                    cursor.executemany("""                
                    insert into {0} values ({1})""".format(table, ','.join('?' * 8)), data.values.tolist())
                table_end = time.time()
                delta_minutes = round((table_end-table_start)/60, 2)
                tables_time[table_name] = delta_minutes
                print('Done processing data into {0}.{1} in {2} minutes'.format(self.dwh_schema, table_name, delta_minutes))
                cursor.commit()
        end_time = time.time()
        print(tables_time)
        print("""
        
        Processed all data in {0} minutes
        -----------------------------------
        """.format(round((end_time-start_time/60),2)))
    def complete(self):
            # Make sure you return false when you want the task to run.
            # And true when complete

            return  self.task_complete


if __name__ == '__main__':
    luigi.run()
