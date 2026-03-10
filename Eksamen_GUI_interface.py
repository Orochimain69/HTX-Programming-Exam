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

# set of buttons for main menu
custom_font_button = tkfont.Font(family='Arial', size=18)
button_PLAY = tk.Button(root, text="PLAY", height=None, width=20, font=custom_font_button)
button_PLAY.pack()

button_SETINGS = tk.Button(root, text='SETINGS', height=None, width=15, font=custom_font_button)
button_SETINGS.pack(pady=50)

button_QUIT = tk.Button(root, text='QUIT', height=None, width=15, font=custom_font_button)
button_QUIT.pack(pady=50)




root.mainloop()

