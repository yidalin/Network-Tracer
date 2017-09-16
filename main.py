# -*- coding: UTF-8 -*-

import os
import time
import subprocess
import re

# mtr 8.8.8.8 -rwz -c 3 -o "SRDL ABW MX"


def main(server='8.8.8.8', protocol='icmp', port='', count='3', output_path='./test.txt'):

    base_mtr_command = 'sudo mtr ' + server + ' -rwz -c ' + count + ' -o "SRDL ABW MX" --json > ' + output_path

    if protocol == 'icmp':
        print(base_mtr_command)
        newprocess = subprocess.getoutput(base_mtr_command)

        # print("stdoutdata: " + stdoutdata.split()[0])
        # new_process = subprocess.Popen(base_mtr_command, shell=True, stdout=subprocess.PIPE)
        # last_line = new_process.stdout.read()

    if protocol == 'tcp':
        base_mtr_command += "--tcp "
    elif protocol == 'ucp':
        base_mtr_command += "-udp "

    if protocol != 'icmp' and ( 0 < port <= 65535):
        base_mtr_command += "-P " + str(port) + " "


main()

cwd = os.getcwd()
print(cwd)

f = open('test.txt', 'r')
print(f.read())
f.close()
