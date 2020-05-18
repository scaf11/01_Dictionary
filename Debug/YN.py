answer = str(input("\n Do you want to enter other world(Yes/No): ")).lower().strip()
print(answer)
print(answer[0])

#while answer[0] != "n":

if answer[0] != "n" and answer[0] != "y":
    print("nok")
else:
    print("ok")