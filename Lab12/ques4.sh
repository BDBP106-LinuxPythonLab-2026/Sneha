#!/bin/bash

read -ra numbers < nums.txt

echo "Elements of the array:"
for num in "${numbers[@]}"
do
    echo $num
done

echo "Doubled values:"
for num in "${numbers[@]}"
do
    result=$((num * 2))
    echo $result
done
