import json

#main
word = input("Enter word: ")
data = json.load(open("../data.json"))

if word in data:
    print(word, ": ", data[word])
elif word.title() in data:
    print(word.title(), ": ", data[word.title()])
else:
    print("Nu e")