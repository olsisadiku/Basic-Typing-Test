import tkinter as tk
from random import randint
import time

top = tk.Tk()
top.geometry("600x400")
top.title("Typing Test")
top.config(bg="black")
phrases = ["The quick brown fox jumps over the lazy dog",
           "Please take your dog, Cali, out for a walk, he really needs some exercise!",
           "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
           "The two boys collected twigs outside, for over an hour, in the freezing cold!",
           "I have three things to do today: wash my car, call my mother, and feed my dog.",
           "The sharper the berry, the sweeter the wine.", "All work and no play robs one of some fun in life.",
           "One morning I shot an elephant in my pajamas. How he got into my pajamas I’ll never know.",
           "The complex houses married and single soldiers and their families."]
phrase_picked = randint(0, len(phrases)-1)
title = tk.Label(top, text= "BASIC TYPING TEST")
title.config(fg= "blue", font= ("Times 32", 30), bg = "black")
title.place(relx= .2, rely = .1)
label = tk.Label(top, text=phrases[phrase_picked])
label.config(font=("Times 32", 12), bg="black", fg="white")
label.place(relx=0.5, rely=.3, anchor="n")
mEntry = tk.Entry(top, width=75, highlightcolor="yellow", highlightthickness=2)
mEntry.config(fg="white", bg="black")
mEntry.place(relx=0.5, rely=.4, anchor="n")

timer = [0]
def percent():
    entry_made = mEntry.get()
    if(len(entry_made) >= len(phrases[phrase_picked])):
        counter = 0
        for i in range(len(phrases[phrase_picked])):
            d = phrases[phrase_picked]
            if (d[i] == entry_made[i]):
                counter += 1
        percent_correct = (counter / len(d))*100
        label3 = tk.Label(top, text="Accuracy: %.d%%"% percent_correct)
        label3.config(bg= "black", fg = "red",font = ("Times 32", 16))
        label3.place(relx=.18, rely=.53)
        label4 = tk.Label(top, text=("Time: %.2f seconds" % timer[-1]))
        label4.config(bg= "black", fg = "blue",font = ("Times 32", 16));
        label4.place(relx=.48, rely=.53)
    else:
        if (len(entry_made) > 0):
            p = timer[-1] + .1
            timer.append(p)
        top.after(100, percent)

    return True

def times(p):
    entry_made = mEntry.get()
    while(len(entry_made) > 0):
        time.sleep(.001)
        p+=.001
        label4 = tk.Label(top, text=("%.f seconds" % p))
        label4.config(fg = "white");
        label4.place(relx=.25, rely=.5)

    else:
        time.sleep(.001)



top.after(500, percent)

top.mainloop()
