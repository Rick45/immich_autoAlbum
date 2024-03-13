
from pathlib import Path
import json
import immichAPI
import json
import loggerManager

try:
  
  logger = loggerManager.get_module_logger('immichiAutoAlbum.py')
  filepath = Path(__file__).parent / 'config.json'

  with open(filepath, 'r') as f:
      immichConfig = json.load(f)

  accountNumber = 0
  isFirstRun = immichConfig["isFirtsRun"]
  for account in immichConfig["accounts"]:
    #logger.info(f'Account: {account}')
    logger.info(f'Account Name: {account["accoutnName"]}')
    ricardo_uuid = '9cdaf934-9f92-43a8-b79d-4a4f71640db3'

    for album in account["albuns"]:
      #logger.info(f'Album: {album}')
      logger.info(f'Album Name: {album["name"]}')
      logger.info(f'Album UUID: {album["id"]}')

      for person in album["persons"]:
        #logger.info(f'Person: {person}')
        logger.info(f'Person Name: {person["name"]}')
        logger.info(f'Person UUID: {person["id"]}')

        
        ids = []
        initialPersonData = immichAPI.searchMetadataByPersonUUID(accountNumber, person["id"], 1)
        assets = initialPersonData["assets"]
        for initialAsset in assets["items"]:
          ids.append(initialAsset["id"])

        # if is the firts run, get all assets, for the remaining runs, only the most recent assets(200) are added
        if isFirstRun:
          while initialPersonData["assets"]["nextPage"] != None:
            assets = initialPersonData["assets"]
            initialPersonData = immichAPI.searchMetadataByPersonUUID(accountNumber, person["id"], assets["nextPage"])

            for asset in initialPersonData["assets"]["items"]:
              ids.append(asset["id"])
          

        data = {
          'ids': ids
        }

        immichAPI.addAssetsToAlbum(accountNumber, album["id"], data)

    print('Done')
    accountNumber += 1


  





except Exception as e:
  # code to handle the exception
  logger.error(f'Error: {e}')