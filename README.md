# financial_statements_elt
This is an Extract-Load-Transform pipeline built on top of Luigi that gather financial statements data since 2011 from http://dados.cvm.gov.br (Comissão de Valores Mobiliários), load it into a SQL Server Databas and process it to make the data more ready for comsuption.


## Getting Started
### Setting up the database
### Setting up the Environment
### Running the Pipeline

```
PYTHONPATH='.' luigi --module main ProcessData

```
### Scheduling the Pipeline

## Results
After running the commands above, you'll have:
-   A SQL Server Database running inside a docker container on your machine with two schemas: financial_statements (raw data) and dwh (processed data)
-   A luigi pipeline with thw whole process broken into tasks.
-   A cron job that runs that process every month to get the latest data

## What you can do with it?
Access thousands of documents of listed companies on B3 within a single query and make analysis of some company financial health very quickly