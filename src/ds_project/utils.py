import os
import sys 
from src.ds_project.logger import logging
from src.ds_project.exception import customexp
from dotenv import load_dotenv
import pandas as pd 
from dataclasses import dataclass
import pymysql 

import logging
import pandas as pd
from sqlalchemy import create_engine

def read_sql_data():
    try:
        engine = create_engine("mysql+pymysql://root:asd123@localhost/collage")
        
        logging.info("Connection established successfully")

        df = pd.read_sql("SELECT * FROM student", engine)

        return df

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise customexp(e,sys)


