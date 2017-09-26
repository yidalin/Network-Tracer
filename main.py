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

mtr_json = main(server='168.95.1.1', count='10')

total_count = len(mtr_json['report']['hubs'])

# print(">> Saving data to sqlite database...")
sqlite_connnect('db_schema.json')
sqlite_create_table('db_schema.json', 'tracer')


base_mtr = mtr_json['report']['mtr']
base_hubs = mtr_json['report']['hubs']

for hop in range(0, total_count):
    src_host = base_mtr['src']
    dst_host = base_mtr['dst']
    host = base_hubs[hop]['host']
    as_number = base_hubs[hop]['ASN']
    packet_count = base_hubs[hop]['count']
    packet_snt = base_hubs[hop]['Snt']
    packet_rcv = base_hubs[hop]['Rcv']
    packet_drop = base_hubs[hop]['Drop']
    packet_loss = base_hubs[hop]['Loss%']
    latency_avg = base_hubs[hop]['Avg']
    latency_best = base_hubs[hop]['Best']
    latency_wrst = base_hubs[hop]['Wrst']

    insert_data = "'{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}".\
        format(current_time, src_host, dst_host,
               host, as_number, packet_count, packet_snt, packet_rcv, packet_drop, packet_loss,
               latency_avg, latency_best, latency_wrst)

    sqlite_insert_data('db_schema.json', 'tracer', insert_data)

    if hop == 0:
        print(">> Inserting data...\n")

    print(insert_data)
    hop += 1

print(">> Disconnecting the SQLite database...")
sqlite_close()
