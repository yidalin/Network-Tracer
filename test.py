import json
from pprint import pprint

with open('test.txt') as f:
    data = json.load(f)

data = dict(data)
len = len(data['report']['hubs'])

for i in range(0, len):
    print(data['report']['hubs'][i]['count'])
    print(data['report']['hubs'][i]['host'])
    print(data['report']['hubs'][i]['ASN'])
    print(data['report']['hubs'][i]['Snt'])
    print(data['report']['hubs'][i]['Rcv'])
    print(data['report']['hubs'][i]['Drop'])
    print(data['report']['hubs'][i]['Loss%'])
    print(data['report']['hubs'][i]['Avg'])
    print(data['report']['hubs'][i]['Best'])
    print(data['report']['hubs'][i]['Wrst'])
    i += 1

