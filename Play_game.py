import tkinter as tk

from tkinter import Label

import exam_project as ex



#
#exam_project.Game_start()


root = tk.Tk()

#text = Text(root, height = 5, width = 52)

while True:
    
    question, answer = ex.Question_maker()

    answer1 = answer + 1
    answer2 = answer - 1



    l = tk.Label(root,
                 text = question
                 )

    l.config(font =("Courier", 12))


    Correctsvar = tk.Button(root,
                   text = answer,
                   command=lambda:ex.Answer_checking(answer,answer)
                   )

    Andetsvar = tk.Button(root,
                   text = answer1,
                   command=lambda:ex.Answer_checking(answer1, answer)
                   )

    Tredjesvar = tk.Button(root,
                   text = answer2,
                   command=lambda:ex.Answer_checking(answer2, answer)
                   )



    l.pack()
    Correctsvar.pack()
    Andetsvar.pack()
    Tredjesvar.pack()

    tk.mainloop()
