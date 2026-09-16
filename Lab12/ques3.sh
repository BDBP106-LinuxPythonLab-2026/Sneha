#!/bin/bash

read -p "Enter a number: " num

i=1

until [ $i -gt 15 ]
do
    result=$((num * i))
    echo "$num x $i = $result"
    ((i++))
done
