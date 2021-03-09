
import luigi
import logging
import pyodbc
import csv
import requests
import zipfile
from io import BytesIO


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
            response_itr = requests.get('http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_' + year +'.zip', stream = True)
            if response_itr.ok:
                z = zipfile.ZipFile(BytesIO(response_itr.content))
                print('Succesfully downloaded {0} itr data'.format(year))
                z.extractall('data')
                print('Finished extracting itr data from {0}'.format(year))
                
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
        return [DownloadCSVs]
    def output(self):
        return luigi.LocalTarget([self.table_names, self.years])
    def run(self):
        
        file_prefixes = ["itr_cia_aberta", 'dfp_cia_aberta']
        self.years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        table_suffixes = ['BPA_con']#['', 'BPA_con', 'BPA_ind', 'BPP_con', 'BPP_ind', 'DFC_MD_con', 'DFC_MD_ind', 'DFC_MI_con', 'DFC_MI_ind', "DMPL_con", "DMPL_ind", "DRE_con", "DRE_ind", "DVA_con", "DVA_ind"]
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
                        print(columns)
                        query = 'insert into {0}.{1}({2}) values ({3})'
                        query = query.format(self.dwh_schema, table_name, ','.join(columns), ','.join('?' * len(columns)))
                        cursor = cnxn.cursor()
                        logging.info("Inserting rows into Postgres with this query:")
                        logging.info(query)
                        for data in reader:
                            data.append(year)
                            print(data)
                            cursor.execute(query, data) # accumulate rows on cursor before inserting
                        cursor.commit()
                        logging.info("Done loading data from {1} into {0}.".format(table_name, year))
    
class ProcessData(luigi.Task):
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
        return []

    def output(self):
        return None

    def run(self):
        #table_names = self.input()[0]

        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=localhost, 1433;"
                      "Database=master;"
                      "UID=SA;"
                      "PWD=<YourStrong@Passw0rd>;")

        sql_paths = ['select_itr_bpa_con.sql']

        file_prefixes = ["itr_cia_aberta", 'dfp_cia_aberta']
        self.years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        table_suffixes = ['BPA_con']#['', 'BPA_con', 'BPA_ind', 'BPP_con', 'BPP_ind', 'DFC_MD_con', 'DFC_MD_ind', 'DFC_MI_con', 'DFC_MI_ind', "DMPL_con", "DMPL_ind", "DRE_con", "DRE_ind", "DVA_con", "DVA_ind"]
        self.table_names = [file_prefix + '_' + table_suffix for table_suffix in table_suffixes for file_prefix in file_prefixes]
        
        for table_name, sql_path in zip(self.table_names, sql_paths):
                for year in self.years:         
                    with open('sql/' + sql_path , 'r') as file:
                        sql = file.read()    
                        print(sql)       
                    query = """
                    with table as ({0})
                    insert into {1}.{2} from table""".format(sql, self.dwh_schema, table_name)
                    cursor = cnxn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                    logging.info("Done processing data from {1} into {0}.".format(table_name, year))
    

if __name__ == '__main__':
    luigi.run()