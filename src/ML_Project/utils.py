import os
import sys
from src.ML_Project.exeception import CustomException
from src.ML_Project.logger import logging 
from dotenv import load_dotenv
import pandas as pd
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("passsword")
db = os.getenv("db")




def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host= host,
            user = user,
            password=password,
            db = db
        )

        logging.info("Connection Established",mydb)
        df = pd.read_sql_query("Select * from students", mydb)
        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex)


