import json


with open('test.txt') as f:
    data = json.load(f)
    ex = data['report']['hubs']
    print(ex)


