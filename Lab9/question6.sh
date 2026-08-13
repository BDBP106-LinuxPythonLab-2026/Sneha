#!/bin/bash

echo $HOME

bc_output=$(bc << EOF
scale=5
23934/44343
EOF
)
echo $bc_output

cd /home/ibab
ls D*

cd /etc
grep "ibab" /etc/passwd

