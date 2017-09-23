#!/bin/bash

echo -e "\t1: Check the wget
\t2: Check the mtr"

echo -n "Please choose one option: "
read choice

if [ ${choice} -eq '1' ]; then
    echo "You choose wget"
elif [ ${choice} -eq '2' ]; then
    echo "You choose mtr"
fi
