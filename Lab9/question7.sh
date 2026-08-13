#!/bin/bash

mass=1
speed=3*10^8
energy=$(bc << EOF
scale=5
$mass*$speed*$speed
EOF
)
echo $energy
