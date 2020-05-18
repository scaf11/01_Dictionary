import json
from difflib import get_close_matches

#definitie_cuvant()
#it gives the definition of the word
def definitie_cuvant(cuvant):
    if  cuvant in data:
        return print_word(cuvant)
    else:
        return best_m(cuvant)


#print_word()
#printing the word and asking if another, with flag
def print_word(cuv):
    print(cuv, ": ", data[cuv])
    answer = str(input("\n Do you want to enter other word(Yes/No): ")).lower().strip()
    while answer[0] != "y" and answer[0] != "n":
        answer = str(input("\n Do you want to enter other word(Yes/No): ")).lower().strip()
    if answer[0] == "y":
        flag_f = 1
    else:
        flag_f = 0
    return flag_f


#get similar matches
def best_m(cu):
    zet = get_close_matches(cu, data.keys())
    print("Did you want to refer to one of following words? ", zet)
    user_input = input("If yes, which one? If no press any keyword: ")
    if user_input.lower() == zet[0]:
        return print_word(user_input.lower())
    elif user_input.lower() == zet[1]:
        return print_word(user_input.lower())
    elif user_input.lower() == zet[2]:
        return print_word(user_input.lower())
    else:
        answer_b = str(input("\n Do you want to enter other word(Yes/No): ")).lower().strip()
        while answer_b[0] != "y" and answer_b[0] != "n":
            answer_b = str(input("\n Do you want to enter other word(Yes/No): ")).lower().strip()
        if answer_b[0] == "y":
            flag_f1 = 1
        else:
            flag_f1 = 0
        return flag_f1


#main
word = input("Enter word: ")
data = json.load(open("../data.json"))
flag = definitie_cuvant(word.lower())
#check if user want another word to check (flag==1)
while flag == 1:
    word = input("\n Enter word: ")
    flag = definitie_cuvant(word.lower())

