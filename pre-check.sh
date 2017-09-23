#!/bin/bash

echo -e "1: Check the wget
2: Check the mtr"

echo -e "Please choose one option:"
read choice

if [ ${choice} -eq '1' ]; then
    echo "You choose wget"
fi
