# **************** Cosing: utf-8 ************

import os
import dotenv import find_dotenv, load_dot_env
import requests
from kaggle.api.kaggle_api_extended import KaggleApi
import logging

# Payload to log into kaggle

payload = {
    'action': 'login',
    'username': os.getenv('KAGGLE_USERNAME'),
    'password': os.getenv('KAGGLE_APIKEY')
}

def extract_data(url,file_path):
    '''
    Method to extract data
    '''
    
    with session() as c:
        c.post('https://www.kaggle.com/account/login', data=payload)
        with open(file_path, 'w') as handle:
            response = c.get(url, stream=True)
            print(response)
            for block in response.iter_content(1024):
                handle.write(block)

extract_data('https://kaggle.com//titanic/download/train.csv','./train.csv')
        

        
