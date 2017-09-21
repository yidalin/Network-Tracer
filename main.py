# -*- coding: UTF-8 -*-

import os
import time
import subprocess
import json
import sqlite3
from pprint import pprint
from functions import *

# import re


def main(server='8.8.8.8', protocol='icmp', port='', count='3', output_path='./mtr-output.log'):
    # mtr 8.8.8.8 -rwz -c 3 -o "SRDL ABW MX"
    # base_mtr_command = 'sudo mtr ' + server + ' -rwz -c ' + count + ' -o "SRDL ABW MX" --json > ' + output_path
    base_mtr_command = 'sudo mtr ' + server + ' -rwz -c ' + count + ' -o "SRDL ABW MX" --json'

    if protocol == 'icmp':
        newprocess = subprocess.getoutput(base_mtr_command)
        data = json.loads(newprocess)
        return data

    if protocol == 'tcp':
        base_mtr_command += "--tcp "
    elif protocol == 'ucp':
        base_mtr_command += "-udp "

    if protocol != 'icmp' and (0 < port <= 65535):
        base_mtr_command += "-P " + str(port) + " "


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


mtr_json = main(server='168.95.1.1')

'''
with open('test.txt') as f:
    data = json.load(f)

data = dict(data)
'''

total_count = len(mtr_json['report']['hubs'])

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

sqlite_close()
