#!/bin/bash

num="2-2"

if [ -z "$num" ]; then
    echo "The string is empty"
else
    echo "The string is not empty"
fi

if [ -n "$num" ]; then
    echo "The string is empty"
else
    echo "The string is not empty"
fi
