import json
from pprint import pprint

with open('db_schema.json') as f:
    data = json.load(f)

db_file = data['db_file']
instnce = data['db_instance'][0]
table = data['table_schema']['host']


print(db_file)
print(instnce)
print(table)