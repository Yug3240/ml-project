from src.ds_project.logger import logging
from src.ds_project.exception import customexp
import sys 
from src.ds_project.components.data_ingestion import DataIngestion,DataIngestionConfig


if __name__=="__main__":
    logging.info("the excution has  ")
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingesction=DataIngestion()
        data_ingesction.inti_data_ingestion()

    except Exception as e :
        logging.info("custom  exception")
        raise customexp(e,sys)
