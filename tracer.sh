#!/bin/bash

python_ver=$(python3 -V)

if [ $?=='0' ]; then
    echo -e ">> Cool, Python3 exist\n"
    echo -e ">> Current Python version: ${python_ver}\n"
else
    echo ">> Could not found Python3...\n"
    exit
fi

if [ $(which mtr) ]; then
    echo -e ">> The command \"mtr\" exist.\n"
    echo -e ">> Now executing main.py, please wait.\n"
    python3 main.py
else
    echo ">> Could not found mtr...\n"
    exit
fi
