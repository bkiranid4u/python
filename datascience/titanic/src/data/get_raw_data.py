# **************** Cosing: utf-8 ************\n

import os
from dotenv import load_dotenv,find_dotenv
import requests
from kaggle.api.kaggle_api_extended import KaggleApi
import logging

# Payload to log into kaggle

payload = {
    'action': 'login',
    'username': os.getenv('KAGGLE_USERNAME'),
    'password': os.getenv('KAGGLE_APIKEY')
}

def extract_data(competition,fileName, filePath):
    '''
    Method to extract data
    '''    
    api = KaggleApi()
    api.authenticate()
    api.competition_download_file(competition,fileName, filePath)
    

def main(project_dir):
    """
        Main Method
    """
    #Get Logger
    
    logger = logging.getLogger(__name__)
    logger.info('Getting Raw Data')
    
    # competion,dataset name && file path 

    raw_data_path = os.path.join(project_dir,'raw','data')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path,'test.csv')
    
    # Extract data
    extract_data('titanic','train.csv',raw_data_path)
    extract_data('titanic','test.csv',raw_data_path)
    
    logger.info('Downloaded the raw data')

if __name__ == '__main__':
    
    # Getting root directory
    
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir,os.pardir)
    
    # Setup the logger
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    # find .env file automatically by walking up directories until it's found 
    
    dotenv_path = find_dotenv()
    
    # Load up the entries as environment variables
    
    load_dotenv(dotenv_path)
    
    main(project_dir)
    
    
