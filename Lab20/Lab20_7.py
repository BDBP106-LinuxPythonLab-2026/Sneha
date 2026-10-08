#ask user to enter a paragraph
#split a sentence wherever there is a space
#creates an empty dictionary
#iterate through words while removing punctuation and converting everything into lower case
#checks whether the word  exists;
# if it does, increase its count, otherwise add it to the dictionary with a count of 1.
#sorts the words alphabetically and also print both word and count
#Look at every word's count and keep the biggest number
#create an empty list to store the most frequent word(s)
#go through each word and check if its count is equal to the highest count
#if the count is equal, add the word to the list
#print all the most frequent word(s) and their count

paragraph=input("Enter your paragraph: ")

words = paragraph.split(" ")

most_frequent_word={}

for word in words:
    word = word.strip(".,!?:;").lower()

    if word in most_frequent_word:
        most_frequent_word[word]+=1
    else:
        most_frequent_word[word]=1

print("Word frequencies:")
for word, count in sorted(most_frequent_word.items()): #items() gives you both word and count then sorted() puts the words in alphabetical order
    print(word, ":" ,count)

highest_word_count=0
for word, count in most_frequent_word.items():
    if count > highest_word_count:
        highest_word_count=count

most_frequent=[]

for word, count in most_frequent_word.items():
    if count > highest_word_count:
        most_frequent.append(word)

print("Most frequent word(s):")
for word in most_frequent:
    print(word, ":", most_frequent_word[word])
