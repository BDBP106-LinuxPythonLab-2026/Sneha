#!/bin/bash

check_directory()
{
    local dir=$1

    if [ -d "$dir" ]; then
        echo "Directory exists."
        ls "$dir"
    else
        mkdir "$dir"
        echo "Directory did not exist, so it was created."
    fi
}

result=$(check_directory "mydir")

echo "$result"
