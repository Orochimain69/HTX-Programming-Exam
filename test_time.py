
import tkinter as tk


root = tk.Tk()


label = tk.Label(root, width=30, height= 30, )


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

label.grid(row=0, column=1, sticky = "ne")



def Countdown_timer(time_left):
    
    
    if time_left > 0:
    
        time_left = time_left - 1
        
        label.config(text=str(time_left))
        
        print(time_left)
        
        root.after(1000, Countdown_timer, time_left)
    
        





Countdown_timer(30)

root.mainloop()