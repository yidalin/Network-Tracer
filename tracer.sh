#!/bin/bash

python3 -V > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e ">> Cool, Python3 exist"
    echo -e ">> Current Python version: $(python3 -V)\n"
else
    echo -e ">> Could not found Python3..."
    echo -e ">> Now install it..."

    which wget > /dev/null 2>&1

    if [ ! $? -eq '0' ]; then
        echo -e ">> Could not found wget, now install it..."
        yum install -y wget > /dev/null && echo -e 'wget installed\n'
    else
        echo -e "wget location: $(which wget)\n"
    fi

    cd /root

    if [ ! -f ./Python-3.6.2.tar.xz ]; then
        echo -e ">> Now downloading the Python 3.6.2 source code from officical website..."
        wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz -O ./Python-3.6.2.tar.xz > /dev/null 2>&1
    fi
    
    ls -l ./Python-3.6.2.tar.xz

    echo -e ">> Now extracting the Python-3.6.2.tar.xz too /root"
    tar Jxvf Python-3.6.2.tar.xz -C ./ > /dev/null 2>&1
    
    ls -ld Python-3.6.2

    echo -e ">> Now install gcc, make"
    yum install -y gcc make zlib-devel

    echo -e ">> Now compiling the Python 3.6.2"
    cd ./Python-3.6.2
    ./configure --enable-optimizations
    make && make install && python3 -V
fi

which mtr > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e ">> The command \"mtr\" exist."
    #echo -e ">> Now executing main.py, please wait.\n"
    #python3 main.py
else
    echo -e ">> Could not found mtr..."
    echo -e ">> Now installing mtr from yum repo"
    yum install -y mtr > /dev/null 2>&1 && ls -l $(which mtr)
    exit
fi
