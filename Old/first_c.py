import json
from difflib import SequenceMatcher
from difflib import get_close_matches

#definitie_cuvant()
#it gives the definition of the word
def definitie_cuvant(cuvant):
    if  cuvant in data:
        return data[cuvant]
        print_word(cuvant)
    else:
        print("Cuvantul nu exista. Va rog verificati")


#print_word()
#printing the word and asking if another, with flag

def print_word(cuv):
    print(data[cuv])
    answer = input("\n Do you want to enter other world(Yes/No): ")
    while answer != "Yes" or answer != "No":
        answer = input("\n Do you want to enter other world(Yes/No): ")
    if answer == "Y":
        flag_f = 1
    else:
        flag_f = 0
    return flag_f


def comparare(c):
    print(SequenceMatcher(None, "rainn", "rain").ratio())


def best_m(cu):
    print(get_close_matches(cu, data.keys()))


      #  raspuns = input


word = input("Enter word: ")
data = json.load(open("../data.json"))
print(definitie_cuvant(word.lower()))

#flag = print_word(word.lower())
#print(flag)


#comparare(word)
#best_m(word)
