import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk


def main(new_window):
    main_window(new_window)
    

def main_window(new_window):
    # root is Tkinter window
    root = tk.Tk()
    root.title("Matematik Spil")

    # resizeing of window for better visibility
    root.resizable(height = None ,width = None )
    root.geometry('600x400')

    # label is title of game in Tkinter window
    custom_font = tkfont.Font(family='Arial', size=36)
    label = tk.Label(root, text="Matematik Spil", font=custom_font)
    label.pack(
        padx=(0,0),
        pady=(150,100)
        )


    # set of buttons for main menu (PLAY button top)
    custom_font_button = tkfont.Font(family='Arial', size=18)
    button_PLAY = tk.Button(root, text="PLAY", height=None, width=20, font=custom_font_button, command=new_window)
    button_PLAY.pack()


    # label and combobox to select math mode to train
    def select(event):
        selected_item = combo_box.get()
        label.config(text="Selected Mode: " + selected_item)


    label = tk.Label(root, text="Mode Selected:")
    label.pack(pady=10)

    # Create a Combobox widget
    combo_box = ttk.Combobox(
        root,
        values=["Plus", "Minus", "Gange", "Division"],
        state="readonly"
    )
    combo_box.pack(pady=5)

    combo_box.set("Select mode")

    combo_box.bind("<<ComboboxSelected>>", select)


    # setings button (no function, middle)
    button_SETINGS = tk.Button(root, text='SETINGS', height=None, width=15, font=custom_font_button)
    button_SETINGS.pack(pady=(50,20))

    # add back when optimizing with functions
    # def QUIT_button():
    #     root.destroy()
        
    # button that close window when pressed (bottom)   
    button_QUIT = tk.Button(root, text='QUIT', height=None, width=15, font=custom_font_button, command=root.destroy)
    button_QUIT.pack(pady=(50,20))

    root.mainloop()
    
    
def new_window():
    root = tk.Tk()
    root.title("new window")
    
    root.mainloop()
    

if __name__ == "__main__":
    main(new_window)
