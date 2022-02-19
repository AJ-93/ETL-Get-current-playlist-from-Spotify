from logging import exception, raiseExceptions
from sqlite3 import Timestamp
from extract_ETL import *
import pandas as pd
import datetime

    
def check_validity(df:pd.DataFrame) -> bool: 
        if df.empty:
           print("empty data received")
           return False
        else:
            return True  

        if df.isnull:
            df.dropna()

        yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
        yesterday = yesterday.replace(hour=0,minute=0,second=0,microsecond=0)
        timestamp_to_compare = df['played_at'].to_list

        # checking the timestamp of the data, to make sure that data older than 24 hours are rejected
        for timestamp in timestamp_to_compare:
            if datetime.datetime.strptime('%Y-%m-%d') != yesterday :
                raiseExceptions("Data downloaded has older songs than last 24 hours")    
