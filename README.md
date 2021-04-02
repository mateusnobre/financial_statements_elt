# financial_statements_elt
This is an Extract-Load-Transform pipeline built on top of Luigi that gather financial statements data since 2011 from http://dados.cvm.gov.br (Comissão de Valores Mobiliários), load it into a SQL Server Databas and process it to make the data more ready for comsuption.

### Prerequisites
- python 3.8.5
- virtualenv python package (you can installing running pip install virtualenv)
- docker


## Getting Started

clone the repo and enter its directory
```
git clone https://github.com/mateusnobre/financial_statements_elt.git
cd financial_statement_elt
```


### Setting up the database (only if you don't already have a DB for tests) - Require Docker Installed

On Linux: 
https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&pivots=cs1-bash
 
On Windows:
Install Docker and then follow the tutorial above for linux
https://docs.docker.com/docker-for-windows/install/


(This tutorial will create a db with these params by default):
DATABASE=master 
SERVER="localhost, 1433"
UID=SA
PASSWORD=<YourStrong@Passw0rd>

### Setting up Database Connection (here you'll open a .env file and insert DATABASE, SERVER, UID and PASSWORD credentials)

On linux 
```
cp .env.sample .env
nano .env
```
On Windows 
```
copy .env.sample .env
notepad .env
```
### Creating required schemas and tables

- Open a console for your DB (On MySQL Workbench, DataGrip, DBeaver, terminal, etc..)
- Open sql_server_statements.md, 
- Copy all statements and run on your console 

### Setting up the Python Virtual Environment and Installing Required Packages


On both Linux and Windows (make sure to change that you are in the path of the repository working directory) 
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the Pipeline


On the script main.py, you can change the Global Variables YEARS (what years to load data from), FILE_PREFIXES (if you want to process quarterly and/or yearly data) and TABLE_SUFFIXES (what tables to process)

```
luigid
```

Now the Central Luigi Scheduler is up and running on http://localhost:8082/ 

To run the entire Pipeline, you can run the last task
```
PYTHONPATH='.' luigi --module main ProcessData
```

To run the Pipeline until certain task, you can run:
```
PYTHONPATH='.' luigi --module main NameOfTheTask
```


### Scheduling the Pipeline


On Windows:
https://blog.e-zest.com/tutorial-setting-up-cron-job-task-scheduler-in-windows#:~:text=The%20simplest%20way%20to%20create,on%20it%20to%20proceed%20further.

On Linux:

## Results
After running the commands above, you'll have:
-   A SQL Server Database running inside a docker container on your machine with two schemas: financial_statements (raw data) and dwh (processed data)
-   A luigi pipeline with thw whole process broken into tasks.
-   A cron job that runs that process every month to get the latest data


## Checking when the data is updated
We get our data from that site, and here you can check if your desired year data was updated (every week the data is updated with corrections and re-presentations)

http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS
http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS

## What you can do with it?
Access thousands of documents of listed companies on B3 within a single query and make analysis of some company financial health very quickly

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