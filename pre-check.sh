#!/bin/bash

echo -e "\t1: Check the wget
\t2: Check the mtr"

echo -n "Please choose one option: "
read choice

if [ ${choice} -eq '1' ]; then
    echo "You choose wget"

    which wget > /dev/null 2>&1
    if [ ! $? -eq '0' ]; then
        echo -e ">> Could not found wget, now install it..."
        yum install -y wget > /dev/null && echo -e 'wget installed\n'
    else
        echo -e "wget location: $(which wget)\n"
    fi

elif [ ${choice} -eq '2' ]; then
    echo "You choose mtr"

    which mtr > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo -e ">> The command mtr exist."
    else
        echo -e ">> Could not found mtr..."
        echo -e ">> Now installing mtr from yum repo"
        #yum install -y mtr > /dev/null 2>&1 && ls -l $(which mtr)

        if [ ! $(cat /etc/redhat-release | awk -F' ' '{print $1}') -eq 'CentOS' ]; then
            exit
        fi

        yum install -y wget gcc autoconf

        cd /root

        wget ftp://ftp.bitwizard.nl/mtr/mtr-0.92.tar.gz -O ./mtr-0.92.tar.gz

        tar zxvf ./mtr-0.92.tar.gz && cd ./mtr-0.92
        ./configure && make && make install
    fi
fi