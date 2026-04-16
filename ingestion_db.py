import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging configuration
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Database connection
engine = create_engine('sqlite:///inventory.db')


# Function to ingest dataframe into DB
def ingest_db(df, table_name, engine):
    """This function will ingest the dataframe into the table"""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


# Function to load CSVs and ingest
def load_raw_data():
    """This function will load the CSVs as dataframe and ingest into DBs"""
    
    start = time.time()

    for file in os.listdir('C:/Users/hp/Downloads/data/data'):
        if file.endswith('.csv'):
            
            file_path = os.path.join('C:/Users/hp/Downloads/data/data', file)

            df = pd.read_csv(file_path)

            logging.info(f'Ingesting {file} into DB')

            ingest_db(df, file[:-4], engine)

    end = time.time()
    total_time = (end - start) / 60

    logging.info('----------- Ingestions Complete ----------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')


# Run the script
if __name__ == '__main__':
    load_raw_data()