import time, json, sqlite3
from pprint import pprint
from functions import *

current_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

database = 'tracer.sqlite'
table = 'tracer'
column = \
    'datetime SMALLDATETIME, ' \
    'src_host TEXT, ' \
    'dst_host TEXT, ' \
    'count TINYINT, ' \
    'host TEXT, ' \
    'as_number TEXT, ' \
    'packet_snt INT, ' \
    'packet_rcv INT, ' \
    'packet_drop INT, ' \
    'packet_loss NUMERIC, ' \
    'latency_avg NUMERIC, ' \
    'latency_best NUMERIC, ' \
    'latency_wrst NUMERIC'


with open('test.txt') as f:
    data = json.load(f)

data = dict(data)
total_count = len(data['report']['hubs'])

sqlite_connnect(database)
sqlite_create_table(table, column)

for i in range(0, total_count):
    count = data['report']['hubs'][i]['count']
    src_host = data['report']['mtr']['src']
    dst_host = data['report']['mtr']['dst']
    host = data['report']['hubs'][i]['host']
    as_number = data['report']['hubs'][i]['ASN']
    packet_snt = data['report']['hubs'][i]['Snt']
    packet_rcv = data['report']['hubs'][i]['Rcv']
    packet_drop = data['report']['hubs'][i]['Drop']
    packet_loss = data['report']['hubs'][i]['Loss%']
    latency_avg = data['report']['hubs'][i]['Avg']
    latency_best = data['report']['hubs'][i]['Best']
    latency_wrst = data['report']['hubs'][i]['Wrst']

    insert_data = "'{}', '{}', '{}', {}, '{}', '{}', {}, {}, {}, {}, {}, {}, {}".format(current_time, src_host, dst_host, count, host, as_number, packet_snt, packet_rcv, packet_drop, packet_loss, latency_avg, latency_best, latency_wrst)
    sqlite_insert_data(table, insert_data)

    i += 1

#query_result = sqlite_query_all(table)
sqlite_close()

#print(query_result[5])
