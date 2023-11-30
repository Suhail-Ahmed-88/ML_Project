from src.ML_Project.logger import logging
from src.ML_Project.exeception import CustomException
from src.ML_Project.components.data_ingestion import DataIngestion
from src.ML_Project.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("The execution has started")


    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("custom Exception")
        raise CustomException(e, sys)

