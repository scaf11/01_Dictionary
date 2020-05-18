"""
This is the GUI version of the English Dictionary python program
It will be have a GUI and it will have also a .exe file
"""

import tkinter
import json
from difflib import get_close_matches

# Loading the database file
data = json.load(open("data.json"))

# Creating the GUI interface (front end)
# main windows
window = tkinter.Tk()
window.geometry("250x400")
window.title("English Dictionay")
zet1=[]


# function of the programm
def definitie():
    # clear text box
    t1.delete(1.0,tkinter.END)
    # read from entry box
    cuv = e1_value.get()
    if cuv.lower() in data:
        t1.insert(tkinter.END, data[cuv.lower()])
    elif cuv.title() in data:
        t1.insert(tkinter.END, data[cuv.title()])
    elif cuv.upper() in data:
        t1.insert(tkinter.END, data[cuv.upper()])
    else:
        best_m(cuv)


def definitie_bm1():
    #print(data[zet1[0]])
    t1.delete(1.0, tkinter.END)
    t1.insert(tkinter.END, data[zet1[0]])

def definitie_bm2():
    t1.delete(1.0, tkinter.END)
    t1.insert(tkinter.END, data[zet1[1]])

def definitie_bm3():
    t1.delete(1.0, tkinter.END)
    t1.insert(tkinter.END, data[zet1[2]])

# if word is not in data, offer 3 close variants
def best_m(cuv):
    zet = get_close_matches(cuv, data.keys())
    zet1.append(zet[0])
    zet1.append(zet[1])
    zet1.append(zet[2])
    l2 = tkinter.Label(window, text="Did you mean:?")
    l2.grid(row=3, column=1)
    bm1 = tkinter.Button(window, text=zet[0], command=definitie_bm1)
    bm1.grid(row=4, column=1)
    bm2 = tkinter.Button(window, text=zet[1], command=definitie_bm2)
    bm2.grid(row=5, column=1)
    bm3 = tkinter.Button(window, text=zet[2], command=definitie_bm3)
    bm3.grid(row=6, column=1)


# create the Button
b1 = tkinter.Button(window, text="Definition", command=definitie)
b1.grid(row=1, column=1, columnspan=2)

# create label of the button
l1 = tkinter.Label(window,text="Word:")
l1.grid(row=0, column=1)

# create the entry
e1_value = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=e1_value, width=20)
e1.grid(row=0, column=2)

# create the text
t1 = tkinter.Text(window, height=20, width=33)
t1.grid(row=2,column=1,columnspan=2,padx=3)


# main
window.mainloop()
