import tkinter as tk

from tkinter import Label


root = tk.Tk()

#text = Text(root, height = 5, width = 52)


l = tk.Label(root, text = "2+2")
l.config(font =("Courier", 12))


b1 = tk.Button(root, text = "4",)

b2 = tk.Button(root, text = "5",)


l.pack()
b1.pack()
b2.pack()

tk.mainloop()
