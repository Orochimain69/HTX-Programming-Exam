import tkinter as tk

from random import randint as rint
from random import shuffle as shuffl
import tkinter.font as tkfont
from tkinter import Label
from tkinter import PhotoImage

from math import ceil

import time

import exam_project as ex



"""
1.1^x as the time function, for points, remember to use math.ceil for rounding up.



use function 0.1x + 1 as the multiplier for correct answers.


"""





#
#exam_project.Game_start()


#root = tk.Tk()
# 
# height = root.winfo_screenheight()+10
# width = root.winfo_screenwidth()+10
# 
# root.geometry(f'{width+1}x{height}')

#this is used later, for stopping the timer. using root.timer_status, to assign variable to root, instead of doing GLOBAL.
#as root is just another object.


#root.timer_status = None


#tried to do something to expand buttons and text according to screen size but found another way that worked
#root.geometry("300x300")
#text = Text(root, height = 5, width = 52)

def Start(root, difficulty):
    

    Question_label = tk.Label(root,
                              )

    #time_label = tk.Label(root,
                          #)



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
    root.grid_rowconfigure(list(range(15)), weight = 1)


    Question_label.grid(row=2, column=5, sticky="nsew" )


    Correctsvar.grid(row=3, column=5, sticky="nsew" )


    Andetsvar.grid(row=4, column=5, sticky="nsew" )


    Tredjesvar.grid(row=5, column=5, sticky="nsew" )



    """

    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    HUSK AT KIGGE PÅ IMAGE, NÅR DU ER FÆRDIG MED RESTEN OG HUSK AT SLETTE

    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    """


    #root.grid_rowconfigure(0, weight=1)
    #root.grid_columnconfigure(0, weight=1)
    #time_label.grid(row = 0, column=0, sticky="ne" )

    #time_label.grid(row=1, column=7, sticky="ne" )
    #image_label.grid(row=3, column=1, sticky="e")

    """
    using after to make 1 second pass, so that the countdown is in seconds. configures time text so user can see the time left.
    """

    """

    so with the help from some searches and some other peoples examples of classes, i have figured out that if something is inside
    a class it needs either self, Timing_and_points or another object. i have looked at it for 4 hours now and holy shit it is hard


    """
    class Timing_and_points:
        def __init__(self):
            #self.time_left = time_left
            #self.points = points
            
            self.root = root
            
            
            """
            Timer
            """
            self.timer_status = None
            
            self.time_label = tk.Label(root,
                          )
            self.time_label.grid(row=0, column=7, sticky="ne", pady=100)
            
            self.time_label.config(font=("Arial", 30))
            """
            Timer
            """
            
            
            """
            highscore
            """
            
            self.Highscore = 0
            
            self.Highscore_Heading = tk.Label(root,
                                              )
            self.Highscore_Heading.grid(row=2, column=7, sticky="ne",)
            
            self.Highscore_Heading.config(text="Highscore")
            
            
            self.Highscore_points = tk.Label(root,
                                            )
            self.Highscore_points.grid(row=2, column=7, sticky="se",) 
            
            self.Highscore_points.config(text= self.Highscore)
            
            self.Times_correct = 0
            

            """
            highscore
            """




        def Timer(self, time_left):
            
            self.time_left = time_left
            
            if time_left >= 0:
                self.time_label.config(text=time_left)
                self.timer_status = root.after(1000, self.Timer, time_left - 1)
            else:
                print("-1 life")
                
        
        
        
        def Timer_stop(self, Boolean):
            
            self.points_system(self.time_left, Boolean)
            
            if self.timer_status != None:
                 root.after_cancel(self.timer_status)
                 self.timer_status = None
        
        
        
        
        def points_system(self, time_left, Boolean):
            
            
            
            def points(self, time_left):
                
                point = 1.13**time_left
                
                return point
                
            def Point_multiplier(self, Times_correct):
                
                
                Multiplier = 0.1*Times_correct+1
                
                return Multiplier
            
            if Boolean == True:
                
                self.Times_correct +=1
                
                
                Multiplier = Point_multiplier(self, self.Times_correct)
                    
                points_earned = points(self, time_left)*Multiplier
                
                Rounded_points_earned = ceil(points_earned)
                
                self.Highscore += Rounded_points_earned
                
                self.Highscore_points.config(text=self.Highscore)
            elif Boolean == False:
                
                Game_Done.lives_lost()
                

                    
            
            
            #print("")
            #print(self.Highscore)
            
        
    class Game_over:
        def __init__(self):
            
            self.lives = 3
            
            
            self.lives_label = tk.Label(root, text= (f'Lives: {self.lives}')
                                        )
            self.lives_label.grid(row=1, column=2)
            
        
        
        def Game_over_screen(self,):
            
            
            for widgets in root.winfo_children():
                widgets.destroy()
            
            self.game_over_label = tk.Label(root,
                                            )
            self.game_over_label.grid(row=2, column=5)
            self.game_over_label.config(text="Game Over", font= ("arial", 20))
            self.Quit_button()
            
            
        def Quit_button(self):
            
            
            button_QUIT = tk.Button(root,
            activebackground="blue",
            activeforeground="white",
            text='QUIT',
            height=None, width=15,
            font=tkfont.Font(family='Arial', size=18),
            command=root.destroy)
            button_QUIT.grid(row=10, column=5, pady=(50,20))
            
            
        
        def lives_lost(self,):
            
            self.lives -= 1
            self.lives_label.config(text= (f'Lives: {self.lives}'))
            
            if self.lives == 0:
                self.Game_over_screen()

            
            
        
        

    # def Timer(time_left):
    #     
    #     if time_left >= 0:
    #         time_label.config(text=time_left)
    #         root.timer_status = root.after(1000, Timer, time_left - 1)
    #     else:
    #         print("-1 life")
    #     
    #     
    # def Timer_stop():
    #     if root.timer_status != None:
    #         root.after_cancel(root.timer_status)
    #     root.timer_status = None 

        


    def New_tkinter_question(TimeClass, difficulty):
        
        
        
        TimeClass.time_label.config(text="30")
        
        question, answer = ex.Question_maker(difficulty)

        answer1 = answer + float(rint(1,4))
        answer2 = answer - float(rint(1,4))
        
        Answer_list = [answer, answer1, answer2]
        
        shuffl(Answer_list)




        Question_label.config(font =("Courier", 12), text=question)



        Correctsvar.config(text = Answer_list[0],
                       command=lambda:(check(Answer_list[0], answer))
                       )




        Andetsvar.config(text = Answer_list[1],
                       command=lambda:(check(Answer_list[1], answer))
                       )



        Tredjesvar.config(text = Answer_list[2],
                       command=lambda:(check(Answer_list[2], answer))
                       )
        
        TimeClass.Timer(30)

    def check(User_answer, correct_answer):
        
        Answer_Check.Answer_checking(Answer_Check, User_answer, correct_answer)
        
        
        
        if  Answer_Check.Answer_Boolean == True:
            Boolean = True
            TimeClass.Times_correct += 1
            print("correct")
        elif Answer_Check.Answer_Boolean == False:
            Boolean = False
            TimeClass.Times_correct = 0
            print("wrong")
        
        TimeClass.Timer_stop(Boolean)
        
        if Game_Done.lives == 0:
            return #makes sure that the program doesnt run the configs with no labels or buttons
        
        
        New_tkinter_question(TimeClass, difficulty)

        
        
        
        #for widget in root.winfo_children():
            #widget.destroy()
    
    Answer_Check = ex.Answer_checker
    TimeClass = Timing_and_points()
    Game_Done = Game_over()
    New_tkinter_question(TimeClass, difficulty)





    #tk.mainloop()

