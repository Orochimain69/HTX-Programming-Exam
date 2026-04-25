import tkinter as tk

from random import randint as rint
from random import shuffle as shuffl

from tkinter import Label
from tkinter import PhotoImage


import time

import exam_project as ex


"""
1.1^x as the time function, for points, remember to use math.ceil for rounding up.



use function 0.1x + 1 as the multiplier for correct answers.


"""





#
#exam_project.Game_start()


root = tk.Tk()

#tried to do something to expand buttons and text according to screen size but found another way that worked
#root.geometry("300x300")
#text = Text(root, height = 5, width = 52)



Question_label = tk.Label(root
                          )

time_label = tk.Label(root,
                      )



Correctsvar = tk.Button(root,
                        )

Andetsvar = tk.Button(root,
                      )

Tredjesvar = tk.Button(root,
                       )

#image_frida = PhotoImage(file="Frida.png")

#image_label = tk.Label(root,
                       #image=image_frida, width=200, height=1000
                       #)



#exitt = tk.Button(root,)




"""
------------------------------------------------------------------------------------------------------------------------------
So i was searching a bunch to see how i would be able to place the timer in the top right of the window, then i found grid.
Tried using it but got an error that basically said that i could use it because "slaves already managed by pack()" which i
a bit funny. Then i just searched as much as i could and found something about adding weight and using sticky for the resizing
for when the window gets resized
"""
root.grid_columnconfigure(list(range(10)), weight = 1,)
root.grid_rowconfigure(list(range(10)), weight = 1)


Question_label.grid(row=1, column=5, sticky="nsew" )


Correctsvar.grid(row=2, column=5, sticky="nsew" )


Andetsvar.grid(row=3, column=5, sticky="nsew" )


Tredjesvar.grid(row=4, column=5, sticky="nsew" )



"""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

HUSK AT KIGGE PÅ IMAGE, NÅR DU ER FÆRDIG MED RESTEN OG HUSK AT SLETTE

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""


#root.grid_rowconfigure(0, weight=1)
#root.grid_columnconfigure(0, weight=1)
#time_label.grid(row = 0, column=0, sticky="ne" )

time_label.grid(row=1, column=7, sticky="ne" )
#image_label.grid(row=3, column=1, sticky="e")


def Timer(time_left):
    
    if time_left > 0:
        time_label.config(text=time_left)
    
        root.after(1000, Timer, time_left - 1)
    else:
        print("-1 life")
    


def New_tkinter_question():
    
    
    
    time_label.config(text="20")
    
    question, answer = ex.Question_maker()

    answer1 = answer + rint(1,4)
    answer2 = answer - rint(1,4)
    
    Answer_list = [answer, answer1, answer2]
    
    shuffl(Answer_list)




    Question_label.config(font =("Courier", 12), text=question)



    Correctsvar.config(text = Answer_list[0],
                   command=lambda:check(Answer_list[0], answer)
                   )




    Andetsvar.config(text = Answer_list[1],
                   command=lambda:check(Answer_list[1], answer)
                   )



    Tredjesvar.config(text = Answer_list[2],
                   command=lambda:check(Answer_list[2], answer)
                   )

    Timer(20)

def check(User_answer, correct_answer):
    ex.Answer_checking(User_answer, correct_answer)
    New_tkinter_question()

    
    
    
    #for widget in root.winfo_children():
        #widget.destroy()
    

New_tkinter_question()





tk.mainloop()

