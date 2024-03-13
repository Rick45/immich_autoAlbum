

from pathlib import Path
import json
import requests
import loggerManager


logger = loggerManager.get_module_logger('immichAPI.py')

filepath = Path(__file__).parent / "config.json"

with open(filepath, 'r') as f:
    configJson = json.load(f)


def getAccoutnConfig(accountNumber):
    obj = type('', (), {})()
    obj.BASE_URL = configJson["accounts"][accountNumber]["url"]
    obj.API_KEY = configJson["accounts"][accountNumber]["apiKey"]
    return obj

def getPersonAssets(accountNumber,person_uuid):
    credentials=getAccoutnConfig(accountNumber)
    url=credentials.BASE_URL + '/person/'+person_uuid+'/assets'
    payload = {}
    headers = {
            'Accept': 'application/json',
            'X-Api-Key': credentials.API_KEY,
            }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:        
        logger.error(f"Error: {response.status_code}")
        logger.error(response.text)
    json_response = response.json()
    return json_response

def getAllAlbums(accountNumber):
    credentials=getAccoutnConfig(accountNumber)
    url=credentials.BASE_URL + '/album'
    payload = {}
    headers = {
            'Accept': 'application/json',
            'X-Api-Key': credentials.API_KEY
            }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:        
        logger.error(f"Error: {response.status_code}")
        logger.error(response.text)
    json_response = response.json()
    return json_response

def addAssetsToAlbum(accountNumber,album_uuid, assets_list):
    credentials=getAccoutnConfig(accountNumber)
    url=credentials.BASE_URL + '/album/'+album_uuid+'/assets'
    payload = json.dumps(assets_list)
    headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': credentials.API_KEY
            }
    response = requests.request("PUT", url, headers=headers, data=payload)
    if response.status_code != 200:        
        logger.error(f"Error: {response.status_code}")
        logger.error(response.text)
    json_response = response.json()
    return json_response

def searchMetadataByPersonUUID(accountNumber,person_uuid, page):
    credentials=getAccoutnConfig(accountNumber)
    if configJson["isFirtsRun"]:
        size = 1000
    else:
        size = 200
    url=credentials.BASE_URL + '/search/metadata'
    requestData = {
          'personIds': [person_uuid],
          'page': page,
          'size': size
        }
    payload = json.dumps(requestData)
    headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': credentials.API_KEY
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200 and response.status_code != 201:        
        logger.error(f"Error: {response.status_code}")
        logger.error(response.text)
    json_response = response.json()
    #logger.info(json_response)
    return json_response