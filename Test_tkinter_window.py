import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window - Center')

window_width = 100
window_height = 200


# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_height)
print(screen_width)


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#label.grid(row=0, column=0, sticky="nsew")


# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


button = tk.Button(root, text = 'height right now', command=lambda: print(root.winfo_height()))

button2 = tk.Button(root, text = 'width right now', command=lambda: print(root.winfo_width()))


button.pack()

button2.pack()

#current_width = root.winfo_width()





root.iconbitmap('./download.ico')



root.mainloop()