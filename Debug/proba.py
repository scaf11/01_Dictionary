import json
from difflib import SequenceMatcher
from difflib import get_close_matches


def definitie_cuvant(cuvant):
    if  cuvant in data:
        return print_word(cuvant)
    else:
        print("Cuvantul nu exista. Va rog verificati")

#print_word()
#printing the word and asking if another, with flag
def print_word(cuv):
    print(data[cuv])
    answer = str(input("\n Do you want to enter other world(Yes/No): ")).lower().strip()
    while answer[0] != "y" and answer[0] != "n":
        answer = str(input("\n Do you want to enter other world(Yes/No): ")).lower().strip()
    if answer[0] == "y":
        flag_f = 1
    else:
        flag_f = 0
    return flag_f


flag = 0
word = input("Enter word: ")
data = json.load(open("../data.json"))
flag = definitie_cuvant(word.lower())
print(flag)


#print(data[word.lower()])