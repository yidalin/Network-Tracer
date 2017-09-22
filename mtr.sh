#!/bin/bash

yum install -y wget gcc autoconf

cd /root

wget ftp://ftp.bitwizard.nl/mtr/mtr-0.92.tar.gz -O ./mtr-0.92.tar.gz

tar zxvf ./mtr-0.92.tar.gz

cd ./mtr-0.92.tar.gz

./configure && make && make install