import json
from difflib import SequenceMatcher
from difflib import get_close_matches

#definitie_cuvant()
#it gives the definition of the word
def definitie_cuvant(cuvant):
    if  cuvant in data:
        return data[cuvant]
    else:
        return best_m(cuvant)



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


#get similar matches
def best_m(cu):
    zet = get_close_matches(cu, data.keys())
    print("Did you want to refer to one of following words? ", zet)
    user_input = input("If yes, which one? If no press any keyword")
    if user_input.lower() == zet[0]:
        return print_word(user_input.lower())
    elif user_input.lower() == zet[1]:
        return print_word(user_input.lower())
    elif user_input.lower() == zet[2]:
        return print_word(user_input.lower())
    else:
        return 1


word = input("Enter word: ")
data = json.load(open("../data.json"))
best_m(word)
#zet = best_m(word.lower())
#print(definitie_cuvant(word.lower()))