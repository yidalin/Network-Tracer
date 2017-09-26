# -*- coding: UTF-8 -*-

import time
from functions import *
'''
import sqlite3
import sys
import os
from pprint import pprint
import json
from getpass import getuser
'''

current_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

mtr_json = main(server='google.com', count='10')

total_count = len(mtr_json['report']['hubs'])

# print(">> Saving data to sqlite database...")
sqlite_connnect('db_schema.json')
sqlite_create_table('db_schema.json', 'tracer')
sqlite_create_table('db_schema.json', 'route')


base_mtr = mtr_json['report']['mtr']
base_hubs = mtr_json['report']['hubs']
hop_list = ""

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
    node += 1

    hop_list = hop_list + "'" + host + "', "

routing = "'{}', '{}', '{}', {}".format(current_time, src_host, dst_host, hop_list[:-2])
print(routing)
print(packet_count)


#sqlite_insert_data('db_schema.json', 'route', routing)


print(">> Disconnecting the SQLite database...")
sqlite_close()
