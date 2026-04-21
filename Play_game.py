import tkinter as tk

from random import randint as rint
from random import shuffle as shuffl

from tkinter import Label

import exam_project as ex


"""
1.1^x as the time function, for points, remember to use math.ceil for rounding up.



use function 0.1x + 1 as the multiplier for correct answers.


"""





#
#exam_project.Game_start()


root = tk.Tk()

#text = Text(root, height = 5, width = 52)
Question_label = tk.Label(root
                          )


Correctsvar = tk.Button(root,
                        )

Andetsvar = tk.Button(root,
                      )

Tredjesvar = tk.Button(root,
                       )


exitt = tk.Button(root,
                  )

Question_label.pack()
Correctsvar.pack()
Andetsvar.pack()
Tredjesvar.pack()






def New_tkinter_question():
    
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



def check(User_answer, correct_answer):
    ex.Answer_checking(User_answer, correct_answer)
    New_tkinter_question()

    
    
    
    #for widget in root.winfo_children():
        #widget.destroy()
    

New_tkinter_question()

tk.mainloop()

