import pandas as pd
from db_config import get_redis_connection
import json
import requests
from requests import Session
import redis



"""
Setup for using Hearthstone API, and loading data into variable.
"""

r = get_redis_connection()

url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/info"

headers = {
	"X-RapidAPI-Key": "c3dac18b96mshf67dcbf531ed4ccp1b6444jsn213ae337a1d2",
	"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

"""
Establishes connection to redis to transfer data too
"""

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

'''
Organize data for ease of use with classes
'''

json_data = r.json().get('info:classes:Mage')
data = json.loads(json_data)



# classes, sets, standard, wild, types, factions, qualities, races, locales

#Classes
# Made with class keyword
# for static, use @staticmethod beofre def

#Classes for Assignment
# Have a class do stuff with data
# Have a class to get stuff from API
# Have a class do json data : class api_json_data

# r = redis.Redis(host='127.0.0.1', port='6379', username = "default", password = "default", ssl = True, decode_responses = True)
# r.set('d2', json.load(response))
# con = connect('c3dac18b96mshf67dcbf531ed4ccp1b6444jsn213ae337a1d2')