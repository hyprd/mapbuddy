import requests, json, math
from os.path import exists
from json import JSONEncoder
from enum import Enum

class ItemEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Item():
    def __init__(self, name, price_chaos, price_divines):
        self.name = name
        self.price_chaos = price_chaos
        self.price_divines = price_divines

endpoint_scarabs = 'https://poe.ninja/api/data/itemoverview?league=Affliction&type=Scarab'
endpoint_compasses = 'https://raw.githubusercontent.com/The-Forbidden-Trove/tft-data-prices/master/lsc/bulk-compasses.json'

Pattern = Enum('Pattern', ['NINJA', 'TFT'])

def fetch_resources():
    fetch_resource(endpoint_scarabs, "data_scarabs.json", Pattern.NINJA)
    fetch_resource(endpoint_compasses, "data_compasses.json", Pattern.TFT)

def fetch_resource(endpoint, output_file, pattern):
    if not exists(output_file):
        data = requests.get(endpoint).json()
        items = []
        match(pattern):
            case Pattern.NINJA:
                for key in data['lines']:
                    item = Item(key['name'], math.ceil(key['chaosValue']), key['divineValue'])
                    items.append(item)
            case Pattern.TFT:
                for key in data['data']:
                    item = Item(key['name'], key['chaos'], key['divine'])
                    items.append(item)
        serialized = json.dumps(items, cls=ItemEncoder, indent=4)
        with open(output_file, 'w') as file:
            file.write(serialized)
        file.close()
    else:
       print("File " + output_file +  " already exists")