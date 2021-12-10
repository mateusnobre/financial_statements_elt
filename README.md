# financial_statements_elt
This is an Extract-Load-Transform pipeline built on top of Luigi that gather financial statements data since 2011 from http://dados.cvm.gov.br (Comissão de Valores Mobiliários), load it into a PostgreSQL database and process it to make the data more ready for comsuption.

### Prerequisites
- python 3.8.5
- pipenv python package (you can installing running `pip install pipenv`)
- docker


## Getting Started

clone the repo and enter its directory
```
git clone https://github.com/mateusnobre/financial_statements_elt.git
cd financial_statement_elt
```


### Setting up the database (only if you don't already have a DB for tests) - Require Docker Installed

On Windows: 
https://www.optimadata.nl/blogs/1/n8dyr5-how-to-run-postgres-on-docker-part-1\



### Setting up Database Connection (here you'll open a .env file and insert DATABASE, SERVER, UID and PASSWORD credentials)

On Linux 
```
cp .env.sample .env
nano .env
```
On Windows 
```
copy .env.sample .env
notepad .env
````

### Install postgres on your machine

On Linux (Ubuntu):
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

### Setting up the Python Virtual Environment and Installing Required Packages


On both Linux and Windows (make sure to change that you are in the path of the repository working directory) 
```
pipenv shell
pipenv install
```

### Running the Pipeline


On the script main.py, you can change the Global Variables YEARS (what years to load data from), FILE_PREFIXES (if you want to process quarterly and/or yearly data) and TABLE_SUFFIXES (what tables to process)

```
python3 main.py
```
### Scheduling the Pipeline


On Windows:
https://blog.e-zest.com/tutorial-setting-up-cron-job-task-scheduler-in-windows#:~:text=The%20simplest%20way%20to%20create,on%20it%20to%20proceed%20further.

## Results
After running the commands above, you'll have:
-   A PostgreSQL Database running inside a docker container on your machine with two schemas: staging (raw data) and data_warehouse (processed data)
-   A cron job that runs that process every month to get the latest data


## Checking when the data is updated
We get our data from that site, and here you can check if your desired year data was updated (every week the data is updated with corrections and re-presentations)

http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS
http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS

## What you can do with it?
Access thousands of documents of listed companies on B3 within a single query and make analysis of some company financial health very quickly


## How to use it -- OUTDATED
You can choose between the 15 tables and write a query like this
```
select *
from dwh.balanco_ativo_ind
where cnpj_cia = '47.508.411/0001-56'
    and quarter in ('2017Q4', '2018Q4', '2019Q4', '2020Q3')
```
Or this to get the data you want of the quarters () you want:

```
select *
from dwh.demonstracao_resultado_ind
where denom_cia = '%NomeDaEmpresa%'
    and quarter in ('CUM_2017Q4', 'CUM_2018Q4', '2019Q2', 'CUM_2020Q3')
```

### Filling the spreadsheet (make sure the CNPJ is in this format: 47.508.411/0001-56) 
```
python fill_excel.py CNPJ_CIA
```


### To-do
☐ Check last modified date on each year before downloading it (tip: use BeautifulSoup)
    http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS
    http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS
☐ Storage optimizations (Create tables to store info from the companies and info from ds_conta strings)
☐ Process DVA, DMPL, DFC_MI, DFC_MD and CIAS_ABERTAS data into the data warehouse (tip: use already existent sql as base, the logic is almost the same)
