import json
from random import *
import names

data = {
    "human": [

    ]
}

def colorGenerator():
    colors = ['white', 'red', 'black', 'yellow', 'brown']
    randNumber = randint(0, 4)
    return colors[randNumber]

def generateHumanObject():
    object = {
        'name': '_',
        'age': 0,
        'color': '_',
        'height': 50,
    }

    object['name'] = names.get_full_name()
    object['age'] = randint(1, 100)
    object['color'] = colorGenerator()
    object['height'] = randint(80, 220)
    
    data['human'].append(object) 


for i in range(1000):
    generateHumanObject()


dataDict = open("data.json", "w")
json.dump(data, dataDict, indent = 6)
dataDict.close()

