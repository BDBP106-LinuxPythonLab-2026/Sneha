if [ -e tall ]; then
    echo "The file exists"
else
    echo "The file does not exist"
fi

if [ -s tall ]; then
    echo "The file exists and is not empty"
else
    echo "The file is empty or does not exist"
fi

if [ -f tall ]; then
    echo "It is a regular file"
else
    echo "It is not a regular file"
fi

# -e checks if the file exits in the particular directory
# -s checks the file size, i.e, if its empty or not
# -f checks it the file is a regular file or not
