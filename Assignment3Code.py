import pandas as pd
from db_config import get_redis_connection
import json
import requests
from requests import Session
import redis
from Assignment3Classes import *




# Setup for using Hearthstone API, and loading data into variable.

r = get_redis_connection()

url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/info"

headers = {
	"X-RapidAPI-Key": "c3dac18b96mshf67dcbf531ed4ccp1b6444jsn213ae337a1d2",
	"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

# Establishes connection to redis to transfer data too

r.json().set(json.dumps(response))

"""
Create a class for future so as to have no code duplication.
"""
class connect:
    def __init__(self, token):
        self.apiurl = 'https://omgvamp-hearthstone-v1.p.rapidapi.com/info'
        self.headers = headers = { 'X-RapidAPI-Key': 'c3dac18b96mshf67dcbf531ed4ccp1b6444jsn213ae337a1d2', 'X-RapidAPI-Host': 'omgvamp-hearthstone-v1.p.rapidapi.com'}
        self.session = Session()
        self.session.headers.update(headers=headers)


# Use classes

basic.query(response)
agr.aggregate(response)
plot.make(response)
