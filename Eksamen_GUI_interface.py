import tkinter as tk
import tkinter.font as tkfont


# root is Tkinter window
root = tk.Tk()
root.title("Matematik Spil")

# resizeing of window for better visibility
root.resizable(height = None ,width = None )
root.geometry('600x400')

# label is title of game in Tkinter window
custom_font = tkfont.Font(family='Arial', size=36)
label = tk.Label(root, text="Matematik Spil", font=custom_font)
label.pack(pady=50)




root.mainloop()

