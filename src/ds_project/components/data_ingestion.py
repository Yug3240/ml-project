import os
import sys 
from src.ds_project.logger import logging
from src.ds_project.exception import customexp
from sklearn.model_selection import train_test_split
import pandas as pd 
from dataclasses import dataclass
from src.ds_project.utils import read_sql_data


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifact','train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data:str=os.path.join('artifact','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def inti_data_ingestion(self):
        try:
            df=read_sql_data()
            logging.info("reading from mysql database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("train split complete")
            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)
        except Exception as e:
            raise customexp(e,sys)

