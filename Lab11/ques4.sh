#!/bin/bash

val1=Jayashree
val2=Nagesh
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi


# in case of if [ $val1 > $val2 ] the shell treated > as an output redirection operator, so it created a new file named Nagesh , hence the result showed “Jayashree is greater than Nagesh”
then after deleting the file named Nagesh using rm command and using if [ $val1 \> $val2 ] in the script > was treated as a string comparison operator , hence the result was “Jayashree is lesser than Nagesh”, and no unwanted file was created.
