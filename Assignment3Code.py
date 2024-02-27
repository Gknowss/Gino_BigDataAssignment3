import requests
import redis
from requests import Session
import json

"""
Setup for using Hearthstone API, and loading data into variable.
"""
url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/info"

headers = {
	"X-RapidAPI-Key": "c3dac18b96mshf67dcbf531ed4ccp1b6444jsn213ae337a1d2",
	"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

'''
Establishes connection to redis to transfer data too
'''
r = redis.Redis(host='127.0.0.1', port='6379', username = "default", password = "default", ssl = True, decode_responses = True)
r.set('d2', json.load(response))

"""
Create a class for future so as to have no code duplication.
"""
class connect:
    def __init__(self, token):
        self.apiurl = 'https://omgvamp-hearthstone-v1.p.rapidapi.com/info'
        self.headers = headers = { 'X-RapidAPI-Key': 'c3dac18b96mshf67dcbf531ed4ccp1b6444jsn213ae337a1d2', 'X-RapidAPI-Host': 'omgvamp-hearthstone-v1.p.rapidapi.com'}
        self.session = Session()
        self.session.headers.update(headers=headers)
    
con = connect('c3dac18b96mshf67dcbf531ed4ccp1b6444jsn213ae337a1d2')



#Classes
# Made with class keyword
# for static, use @staticmethod beofre def

#Classes for Assignment
# Have a class do stuff with data
# Have a class to get stuff from API
# Have a class do json data : class api_json_data