from prefect import task, Flow
import psycopg2
import pandas as pd
import csv
import requests
import time
import zipfile
from io import BytesIO
import os
from os.path import join, dirname
from dotenv import load_dotenv

# retrieving env variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(verbose=True)
DB = os.environ.get("DB")
HOST_URL = os.environ.get("HOST_URL")
DB_USER = os.environ.get("DB_USER")
DB_PWD = os.environ.get("DB_PWD")
PORT = os.environ.get("PORT")

conn = psycopg2.connect(host=HOST_URL,
                        database=DB,
                        user=DB_USER,
                        password=DB_PWD,
                        port=PORT)
cursor = conn.cursor()
# defining the year to extract and process data from
YEARS = [
    '2020'
]  #, '2012', '2013', '2014', '2015','2016', '2017', '2018', '2019', '2020','2021', '2022']

# defining if we want both quartely and yearly data
FILE_PREFIXES = ['itr_cia_aberta', 'dfp_cia_aberta']

# defining the tables that we want to extract and process data from
TABLE_SUFFIXES_DICT = {
    "DMPL_con": 'demonstracao_mutacao_con',
    "DMPL_ind": 'demonstracao_mutacao_ind',
    "DRE_con": 'demonstracao_resultado_con',
    'DRE_ind': 'demonstracao_resultado_ind',
    'BPA_con': 'balanco_ativo_con',
    'BPA_ind': 'balanco_ativo_ind',
    'BPP_con': 'balanco_passivo_con',
    'BPP_ind': 'balanco_passivo_ind',
    'DFC_MD_con': 'demonstracao_fluxo_direto_con',
    'DFC_MD_ind': 'demonstracao_fluxo_direto_ind',
    'DFC_MI_con': 'demonstracao_fluxo_indireto_con',
    'DFC_MI_ind': 'demonstracao_fluxo_indireto_ind',
    "DVA_con": 'demonstracao_valor_adicionado_con',
    "DVA_ind": 'demonstracao_valor_adicionado_ind',
    "": 'cias_abertas'
}

STAGING_SCHEMA = 'staging'
DATA_WAREHOUSE_SCHEMA = 'data_warehouse'


@task
def CreateSchemas():
    sql_preffix = 'create_schemas/'
    sql_path = sql_preffix + 'create_schemas.sql'
    with open('sql/' + sql_path, 'r') as file:
        cursor.execute(file.read().format(
            staging_schema=STAGING_SCHEMA,
            data_warehouse_schema=DATA_WAREHOUSE_SCHEMA))
    conn.commit()


@task
def CreateTables():
    staging_sql_preffix = 'create_tables/staging_schema/create_'
    data_warehouse_sql_preffix = 'create_tables/data_warehouse_schema/create_'

    with open('sql/' + data_warehouse_sql_preffix + 'dimensions.sql',
              'r') as file:
        cursor.execute(file.read().format(schema=DATA_WAREHOUSE_SCHEMA))
    conn.commit()

    for key, val in TABLE_SUFFIXES_DICT.items():
        for file_preffix in FILE_PREFIXES:
            if (key == ''):
                staging_sql_path = staging_sql_preffix + file_preffix + '.sql'
            else:
                staging_sql_path = staging_sql_preffix + file_preffix + '_' + key + '.sql'
            with open('sql/' + staging_sql_path, 'r') as file:
                cursor.execute(file.read().format(schema=STAGING_SCHEMA))
        dwh_sql_path = data_warehouse_sql_preffix + val + '.sql'
        with open('sql/' + dwh_sql_path, 'r') as file:
            cursor.execute(file.read().format(schema=DATA_WAREHOUSE_SCHEMA))
    conn.commit()


@task
def DownloadCSVs():
    years = YEARS
    for year in years:
        if not os.path.isfile('data/itr_cia_aberta_' + year + '.csv'):
            response_itr = requests.get(
                'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_'
                + year + '.zip',
                stream=True)
            if response_itr.ok:
                z = zipfile.ZipFile(BytesIO(response_itr.content))
                print('Succesfully downloaded {0} itr data'.format(year))
                z.extractall('data')
                print('Finished extracting itr data from {0}'.format(year))
        if not os.path.isfile('data/dfp_cia_aberta_' + year + '.csv'):
            response_dfp = requests.get(
                'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_'
                + year + '.zip',
                stream=True)
            if response_dfp.ok:
                z = zipfile.ZipFile(BytesIO(response_dfp.content))
                print('Succesfully downloaded {0} dfp data'.format(year))
                z.extractall('data')
                print('Finished extracting dfp data from {0}'.format(year))


@task
def FromCSVToPostgres():
    table_names = None
    years = YEARS

    file_prefixes = FILE_PREFIXES
    table_suffixes = [key for key, _ in TABLE_SUFFIXES_DICT.items()]
    table_names = [
        file_prefix + '_' + table_suffix if table_suffix != '' else file_prefix
        for table_suffix in table_suffixes for file_prefix in file_prefixes
    ]
    print(table_names)
    tables_time = dict()
    start = time.time()
    years_time = dict()
    for year in years:
        year_start = time.time()
        for table_name in table_names:
            i = 0
            table_start = time.time()
            print("""
                ----------------------------------------------------------------
                """)
            with open('data/' + table_name + '_' + year + '.csv',
                      'r',
                      encoding='unicode_escape') as f:
                reader = csv.reader(f, delimiter=';')
                columns = next(reader)
                columns.append('ano')
                #delete_query = """
                #        delete from {0}.{1} where year(dt_refer) = {2}""".format(dest_schema, table_name, int(year))
                insert_query = """insert into {0}.{1}({2}) values ({3})"""
                insert_query = insert_query.format(
                    STAGING_SCHEMA, table_name, ','.join(columns),
                    ','.join(['%s'] * len(columns)))
                #print("Deleting data from {0} already in the {1} table.".format(year, table_name))
                #cursor.execute(delete_query)
                print("Start loading data from {1} into {0}".format(
                    year, table_name))
                for data in reader:
                    try:
                        data.append(year)
                        cursor.execute(
                            insert_query,
                            data)  # accumulate rows on cursor before inserting
                        i = i + 1
                    except:
                        i = i + 1
                        print("Couldn't process line {0} of {1}_{2}".format(
                            i, table_name, year))

                conn.commit()
                table_end = time.time()
                table_delta_minutes = round(((table_end - table_start) / 60),
                                            2)
                tables_time[table_name] = 0
                tables_time[table_name] += table_delta_minutes
                print("Done loading data from {1} into {0} in {2} minutes.".
                      format(year, table_name, table_delta_minutes))
        year_end = time.time()
        delta_year_hours = round(((year_end - year_start) / 3600), 2)
        years_time[year] = delta_year_hours
        directory = "./data"
        files_in_directory = os.listdir(directory)
        filtered_files = [
            file for file in files_in_directory if file.endswith(year + ".csv")
        ]
        for file in filtered_files:
            try:
                path_to_file = os.path.join(directory, file)
                os.remove(path_to_file)
            except:
                print(
                    "Cannot delete {0}, check if the file exist".format(file))
        print("Year {0} fully processed in {1} hours".format(
            year, delta_year_hours))
        print("""
            ----------------------------------------------------------------
            ----------------------------------------------------------------
            ----------------------------------------------------------------
            """)
    end = time.time()
    print(years_time)
    print(tables_time)
    print("Finished task in {0} hours".format(round((end - start) / 3600), 2))


@task
def ProcessData():
    # defining the sql files that will process each of the tables
    # be aware that the sql_paths order MUST MATCH the table names order
    sql_paths = [
        "select_{0}.sql".format(val) for _, val in TABLE_SUFFIXES_DICT.items()
    ]
    table_names = [val for _, val in TABLE_SUFFIXES_DICT.items()]

    tables_time = dict()
    start_time = time.time()

    with open('sql/process_data/insert_companies.sql', 'r') as file:
        cursor.execute(file.read().format(dw_schema=DATA_WAREHOUSE_SCHEMA,
                                          st_schema=STAGING_SCHEMA))
    conn.commit()

    for table_name, sql_path in zip(table_names, sql_paths):
        with open('sql/process_data/' + sql_path, 'r') as file:
            table_start = time.time()
            sql = file.read().format(dw_schema=DATA_WAREHOUSE_SCHEMA,
                                     st_schema=STAGING_SCHEMA)
            data = pd.read_sql(sql=sql, con=conn)
            table = DATA_WAREHOUSE_SCHEMA + '.' + table_name
            print("Starting processing {0} data".format(table))
            cursor.execute("truncate table {0}".format(table))
            if table_name == 'cias_abertas':
                n_columns = 8
            elif table_name in [
                    'demonstracao_mutacao_con', 'demonstracao_mutacao_ind'
            ]:
                n_columns = 6
            else:
                n_columns = 5

            cursor.executemany(
                """                
                insert into {0} values ({1})""".format(
                    table, ','.join(['%s'] * n_columns)), data.values.tolist())
            table_end = time.time()
            delta_minutes = round((table_end - table_start) / 60, 2)
            tables_time[table_name] = delta_minutes
            print('Done processing data into {0}.{1} in {2} minutes'.format(
                DATA_WAREHOUSE_SCHEMA, table_name, delta_minutes))
            conn.commit()
    end_time = time.time()
    print(tables_time)
    print("""
        
        Processed all data in {0} minutes
        -----------------------------------
    """.format(round(((end_time - start_time) / 60), 2)))


if __name__ == '__main__':
    with Flow("Financial Statements ELT") as flow:
        create_schemas = CreateSchemas()
        create_tables = CreateTables()
        download_csvs = DownloadCSVs()
        from_csv_to_postgres = FromCSVToPostgres()
        process_data = ProcessData()
        flow.set_dependencies(task=process_data,
                              upstream_tasks=[
                                  create_schemas, create_tables, download_csvs,
                                  from_csv_to_postgres
                              ])
        flow.set_dependencies(
            task=from_csv_to_postgres,
            upstream_tasks=[create_schemas, create_tables, download_csvs])
        flow.set_dependencies(task=download_csvs,
                              upstream_tasks=[create_schemas, create_tables])
        flow.set_dependencies(task=create_tables,
                              upstream_tasks=[create_schemas])
    flow.run()
