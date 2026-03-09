import tkinter as tk

# root is Tkinter window
root = tk.Tk()
root.title("Matematik Spil")

# resizeing of window for better visibility
root.resizable(height = None ,width = None )
root.geometry('600x400')

# label is title of game in Tkinter window
label = tk.Label(root, text="Matematik Spil")
label.pack()




root.mainloop()

