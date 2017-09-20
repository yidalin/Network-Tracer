# -*- coding: UTF-8 -*-

import os
import time
import subprocess
import re
import json

# mtr 8.8.8.8 -rwz -c 3 -o "SRDL ABW MX"


def main(server='8.8.8.8', protocol='icmp', port='', count='3', output_path='./test.txt'):

    # base_mtr_command = 'sudo mtr ' + server + ' -rwz -c ' + count + ' -o "SRDL ABW MX" --json > ' + output_path
    base_mtr_command = 'sudo mtr ' + server + ' -rwz -c ' + count + ' -o "SRDL ABW MX" --json'

    if protocol == 'icmp':
        newprocess = subprocess.getoutput(base_mtr_command)

        data = json.loads(newprocess)

        print(data)

    if protocol == 'tcp':
        base_mtr_command += "--tcp "
    elif protocol == 'ucp':
        base_mtr_command += "-udp "

    if protocol != 'icmp' and (0 < port <= 65535):
        base_mtr_command += "-P " + str(port) + " "

main()

'''
dict = {
    "report": {
        "hubs": {
            "time": "time"
        }
    }
}

with open('test.txt', 'a') as f:
    json.dump(dict, f)

cwd = os.getcwd()
print(cwd)
'''
'''
f = open('test.txt', 'r')
print(f.read())
f.close()
'''
