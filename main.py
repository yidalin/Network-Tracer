# -*- coding: UTF-8 -*-

import sys
import os
import time
import subprocess
import json
import sqlite3
from pprint import pprint
from functions import *
from getpass import getuser
# import re

print(">> Now the Python version is {}".format(sys.version))

print(">> Import modules...")

def main(server='8.8.8.8', protocol='icmp', port='', count='3', output_path='./mtr-output.log'):
    # mtr 8.8.8.8 -rwz -c 3 -o "SRDL ABW MX"
    # base_mtr_command = 'sudo mtr ' + server + ' -rwz -c ' + count + ' -o "SRDL ABW MX" --json > ' + output_path

    if getuser() == 'root':
        exec_mtr = 'mtr '
    else:
        exec_mtr = 'sudo mtr '

    mtr_command = exec_mtr + server + ' -nrwz -c ' + count + ' -o "SRDL ABW MX" --json'

    if protocol == 'icmp':
        newprocess = subprocess.getoutput(mtr_command)
        data = json.loads(newprocess)
        return data

    if protocol == 'tcp':
        base_mtr_command += "--tcp "
    elif protocol == 'ucp':
        base_mtr_command += "-udp "

    if protocol != 'icmp' and (0 < port <= 65535):
        base_mtr_command += "-P " + str(port) + " "


print(">> Define variables...")

current_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

database = '/git/Tracer/tracer.sqlite'

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


print(">> Processing main function...")
mtr_json = main(server='168.95.1.1', count='10')

'''
with open('test.txt') as f:
    data = json.load(f)

data = dict(data)
'''

total_count = len(mtr_json['report']['hubs'])


print(">> Saving data to sqlite database...")
sqlite_connnect(database)
sqlite_create_table(table, column)

base_mtr = mtr_json['report']['mtr']
base_hubs = mtr_json['report']['hubs']

for hop in range(0, total_count):
    count = base_hubs[hop]['count']
    src_host = base_mtr['src']
    dst_host = base_mtr['dst']
    host = base_hubs[hop]['host']
    as_number = base_hubs[hop]['ASN']
    packet_snt = base_hubs[hop]['Snt']
    packet_rcv = base_hubs[hop]['Rcv']
    packet_drop = base_hubs[hop]['Drop']
    packet_loss = base_hubs[hop]['Loss%']
    latency_avg = base_hubs[hop]['Avg']
    latency_best = base_hubs[hop]['Best']
    latency_wrst = base_hubs[hop]['Wrst']

    insert_data = "'{}', '{}', '{}', {}, '{}', '{}', {}, {}, {}, {}, {}, {}, {}".\
        format(current_time,src_host, dst_host,
               count, host, as_number, packet_snt, packet_rcv, packet_drop, packet_loss,
               latency_avg, latency_best, latency_wrst)

    sqlite_insert_data(table, insert_data)

    if hop == 0:
        print(">> Inserting data...\n")

    print(insert_data)
    hop += 1

print(">> Disconnecting the SQLite database...")
sqlite_close()
