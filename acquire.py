import pandas as pd
import numpy as np
import os
from env import host, username, password


# Get Connection
def get_connection(db, username=username, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup SQL db.
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

# Get Zillow Data
def zillow_data():
    '''
    This function reads the Zillow data from the Codeup db into a df.  Filters data by Single Unit Property and by date '2017-04-30' AND '2017-08-3'
    '''
    
    # Create SQL query
    sql_query = '''SELECT parcelid, bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet, fips, yearbuilt, taxvaluedollarcnt, taxamount, propertylandusetypeid, transactiondate
                FROM properties_2017
                JOIN predictions_2017 using (parcelid)
                WHERE transactiondate BETWEEN '2017-04-30' AND '2017-08-31'
                AND propertylandusetypeid IN (261, 262, 263, 264, 265, 267, 268, 273, 274, 275, 276, 277, 278, 279);
                '''

    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))

    return df

# Cache'ing Telco Data
def cache_zillow_data(cached=False):
    '''
    This function reads in Zillow data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in iris df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('zillow_df.csv') == False:

        # Read fresh data from db into a DataFrame
        df = zillow_data()

        # Cache data
        df.to_csv('zillow_data.csv')

    else:

        # If csv file exists or cached == True, read in data from csv file.
        df = pd.read_csv('zillow_data.csv', index_col=0)