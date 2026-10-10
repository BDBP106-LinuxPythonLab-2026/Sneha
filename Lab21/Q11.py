"""Write a program to concatenate a list of strings to make a sentence using reduce function."""

from functools import reduce
words=["Python","is","an","easy","language"]
print("Sentence:" ,reduce(lambda x,y: x+" "+y,words))