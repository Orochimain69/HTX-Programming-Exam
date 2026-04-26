#import pygame
import random
import math
import time
import tkinter as tk


User_points = 0



def Question_maker(selected_difficulty):
    
    
    if selected_difficulty == "Svær":
        Question_difficulty = random.randint(3,5)
    elif selected_difficulty == "Medium":
        Question_difficulty = random.randint(2,3)
    elif selected_difficulty == "Let":
        Question_difficulty = random.randint(1,2)
        
        
    
    
    Question = ""
    
    
    List_of_numbers = ['1','2','3','4','5','6','7','8','9','10']
    
    List_of_operators = ['+','-','*','/']
    
    for equation in range(Question_difficulty):
        
        number1 = List_of_numbers[random.randint(0,9)]
        operand = List_of_operators[random.randint(0,3)]
        #number2 = List_of_numbers[random.randint(0,9)]
        
        Question = Question + number1 + operand
    
    number2 = List_of_numbers[random.randint(0,9)]
    
    Question = Question + number2
    
    #Question = List_of_numbers[random.randint(0,9)] + list_of_operators[random.randint(0,3)] + List_of_numbers[random.randint(0,9)]
    
    #Question = '2/3'
    
    
    answer = eval(Question)
    
    divider = 100
    
    if int(
        (
        (float(answer)-int(answer))*10
        )
           )< 5:
        answer= math.floor(answer*divider)/divider
    else:
        answer = math.ceil(answer*divider)/divider
    
    
    print(' ')
    print(Question)
    print(' ')
    print(answer)
    
    return Question, answer
    

    
    
"""
i dont think this class is needed but i couldnt think of another way to do this, the way i wanted it.
"""
    
class Answer_checker:
    
    def __init__(self):
        
        self.Answer_Boolean = True 
        
        
        
    
    def Answer_checking(self, User_answer, correct_answer):
        
        if float(User_answer) == correct_answer:
            self.Answer_Boolean = True
            
            #Question_maker()
        else:
            self.Answer_Boolean = False



#print(question, answer)

# def Answer_checking(User_answer, correct_answer):
#         
#         if float(User_answer) == correct_answer:
#             return "Correct"
#             
#             #Question_maker()
#         else:
#             return 'Wrong'
            #Question_maker()
        #Exit = input('do you wanna exit? ')
     
