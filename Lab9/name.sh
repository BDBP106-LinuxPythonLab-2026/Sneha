#!/bin/bash

echo "My name is $1"
echo "My MSc program is $2"

echo 'The first argument is: ',$1
echo 'The second argument is; ',$2

echo 'The number of arguments passed to this script: '$#
echo 'The array/list of arguments passed to this script; '$@

