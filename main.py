# -*- coding: UTF-8 -*-

import time
from functions import *

current_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

mtr_json = main(server='google.com', count='30')

total_count = len(mtr_json['report']['hubs'])

# print(">> Saving data to sqlite database...")
sqlite_connnect('db_schema.json')
sqlite_create_table('db_schema.json', 'tracer')
sqlite_create_table('db_schema.json', 'route')


base_mtr = mtr_json['report']['mtr']
base_hubs = mtr_json['report']['hubs']

src_host = ''
dst_host = ''

route = ['-'] * 30

for node in range(0, total_count):
    src_host = base_mtr['src']
    dst_host = base_mtr['dst']
    host = base_hubs[node]['host']
    as_number = base_hubs[node]['ASN']
    packet_count = base_hubs[node]['count']
    packet_snt = base_hubs[node]['Snt']
    packet_rcv = base_hubs[node]['Rcv']
    packet_drop = base_hubs[node]['Drop']
    packet_loss = base_hubs[node]['Loss%']
    latency_avg = base_hubs[node]['Avg']
    latency_best = base_hubs[node]['Best']
    latency_wrst = base_hubs[node]['Wrst']

    insert_data = "'{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}".\
        format(current_time, src_host, dst_host,
               host, as_number, packet_count, packet_snt, packet_rcv, packet_drop, packet_loss,
               latency_avg, latency_best, latency_wrst)

    sqlite_insert_data('db_schema.json', 'tracer', insert_data)

    if node == 0:
        print(">> Inserting data...\n")

    print(insert_data)
    print(type(insert_data))
    node += 1

    route[int(packet_count)-1] = host


route_list = [current_time] + [src_host] + [dst_host] + route
route_str = ''

for i in route_list:
    route_str = route_str + ', ' + '\'' + i + '\''

route_str = route_str[2:]

sqlite_insert_data('db_schema.json', 'route', route_str)


print(">> Disconnecting the SQLite database...")
sqlite_close()
