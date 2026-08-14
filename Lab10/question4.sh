#!/bin/bash

echo "enter a number:"
read n

if [ "$n" -ge 1 ]; then
     echo "the number is positive."
elif [ "$n" -le -1 ]; then
     echo "the number is negative."
else
     echo "the number is zero."
fi

