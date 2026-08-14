#!/bin/bash

echo 'Enter file name!'
read file

if [ -f "$file" ]; then
echo 'file exists'
       if [ -x "$file" ]; then 
       echo 'file is executable'
       else
       echo 'file not executable'
       fi
else
echo 'file does not exists'
fi
