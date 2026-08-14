#!/bin/bash

echo "enter a score (0-100):"
read n

if [ "$n" -ge 90 ]; then
     echo 'Grade "A"'
elif [ "$n" -ge 80 ]; then
     echo 'Grade "B"'
elif [ "$n" -ge 70 ]; then
     echo 'Grade "C"'
else
     echo "Fail"
fi

