#!/bin/bash

maximum()
{
    local num1=$1
    local num2=$2

    if [ $num1 -gt $num2 ]; then
        echo $num1
    else
        echo $num2
    fi
}

result=$(maximum 25 40)

echo "Maximum = $result"
