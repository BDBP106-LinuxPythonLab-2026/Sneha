#!/bin/bash

filename='question2.sh'
if [ -f "$filename" ]; then 
  echo 'File exists.'
  exit 200
else
  exit 201
  echo "File does not exist."
fi
echo 'Outside the if-block '
