import requests, math
from enum import Enum

endpoint_scarabs = 'https://poe.ninja/api/data/itemoverview?league=Affliction&type=Scarab'
endpoint_compasses = 'https://raw.githubusercontent.com/The-Forbidden-Trove/tft-data-prices/master/lsc/bulk-compasses.json'

Pattern = Enum('Pattern', ['NINJA', 'TFT'])
        
def fetch_resource(endpoint, pattern):
    data = requests.get(endpoint).json()
    items = {}
    match(pattern):
        case Pattern.NINJA:
            for key in data['lines']:
                items.update({key['name']: math.ceil(key['chaosValue'])})
        case Pattern.TFT:
            for key in data['data']:
                items.update({key['name'] : math.ceil(key['chaos'])})
    return items