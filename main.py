# -*- coding: UTF-8 -*-
import time
import sys
from functions import *


if len(sys.argv) < 3:
    print("Please make sure you give enough arguments")
    sys.exit(1)

current_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

mtr_json = main(server=sys.argv[1], count=sys.argv[2])

total_count = len(mtr_json['report']['hubs'])

# print(">> Saving data to sqlite database...")
# print(">> Connecting the SQLite database.")
sqlite_connnect('/git/Tracer/db_schema.json')

# print(">> Creating table if it is not exist.")
sqlite_create_table('/git/Tracer/db_schema.json', 'tracer')
sqlite_create_table('/git/Tracer/db_schema.json', 'route')


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

    # print(">> Inserting data to tracer table.")
    sqlite_insert_data('/git/Tracer/db_schema.json', 'tracer', insert_data)

    if node == 0:
        print(">> Inserting data...\n")

    node += 1

    route[int(packet_count)-1] = host


route_list = [current_time] + [src_host] + [dst_host] + route
route_str = ''

for i in route_list:
    route_str = route_str + ', ' + '\'' + i + '\''

route_str = route_str[2:]

# print(">> Inserting data to route table.")
sqlite_insert_data('/git/Tracer/db_schema.json', 'route', route_str)

# print(">> Disconnecting the SQLite database.")
sqlite_close()
