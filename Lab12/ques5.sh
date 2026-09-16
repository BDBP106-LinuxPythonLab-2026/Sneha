#!/bin/bash

divide()
{
    local num1=$1
    local num2=$2
    local quotient
    local remainder

    if [ $num2 -eq 0 ]; then
        echo "Error: Division by zero is not allowed"
        return
    fi

    quotient=$(awk "BEGIN {printf \"%.2f\", $num1 / $num2}")
    remainder=$((num1 % num2))

    echo "Quotient = $quotient"
    echo "Remainder = $remainder"
}

result=$(divide 10 3)
echo "$result"
