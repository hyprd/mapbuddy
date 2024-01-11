import requests, json, math
from os.path import exists
from json import JSONEncoder
from enum import Enum

class ItemEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Item():
    def __init__(self, name, price_chaos):
        self.name = name
        self.price_chaos = price_chaos

endpoint_scarabs = 'https://poe.ninja/api/data/itemoverview?league=Affliction&type=Scarab'
endpoint_compasses = 'https://raw.githubusercontent.com/The-Forbidden-Trove/tft-data-prices/master/lsc/bulk-compasses.json'

Pattern = Enum('Pattern', ['NINJA', 'TFT'])
ResourceType = Enum('ResourceType', ['SCARAB', 'COMPASS'])

def fetch_resources():
    fetch_resource(endpoint_scarabs, "data_scarabs.json", Pattern.NINJA)
    fetch_resource(endpoint_compasses, "data_compasses.json", Pattern.TFT)

def fetch_resource_names(resource):
    file = ''
    values = {}
    match(resource):
        case ResourceType.SCARAB: 
            file = 'data_scarabs.json'
        case ResourceType.COMPASS:
            file = 'data_compasses.json'
    with open(file, 'r') as file:
        f = json.load(file)
        for key in f:
            values.update({key['name']: key['price_chaos']})
    file.close()
    return values
        
def fetch_resource(endpoint, output_file, pattern):
    if not exists(output_file):
        data = requests.get(endpoint).json()
        items = []
        match(pattern):
            case Pattern.NINJA:
                for key in data['lines']:
                    item = Item(key['name'], math.ceil(key['chaosValue']))
                    items.append(item)
            case Pattern.TFT:
                for key in data['data']:
                    item = Item(key['name'], key['chaos'])
                    items.append(item)
        serialized = json.dumps(items, cls=ItemEncoder, indent=4)
        with open(output_file, 'w') as file:
            file.write(serialized)
        file.close()
    else:
       print("File " + output_file +  " already exists")