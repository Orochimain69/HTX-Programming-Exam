import pygame
import random
import math
import time
import tkinter as tk


User_points = 0



def Question_maker():
    
    List_of_numbers = ['1','2','3','4','5','6','7','8','9','10']
    
    List_of_operators = ['+','-','*','/']
    
    
    number1 = List_of_numbers[random.randint(0,9)]
    operand = List_of_operators[random.randint(0,3)]
    number2 = List_of_numbers[random.randint(0,9)]
    
    
    
    #Question = List_of_numbers[random.randint(0,9)] + list_of_operators[random.randint(0,3)] + List_of_numbers[random.randint(0,9)]
    
    Question = number1+operand+number2
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
    

    
    
    
    


#print(question, answer)

def Answer_checking(User_answer, correct_answer):
        
        if float(User_answer) == correct_answer:
            print('correct')
            #Question_maker()
        else:
            print('WRONG!!!!')
            #Question_maker()
        #Exit = input('do you wanna exit? ')
        #if Exit == 'y':
            #wee = 2
            #return 0, wee
        
#wee = 1    
#while wee == 1:

#question, answer = Question_maker()
    
#Correct_or_not, wee = Answer_checking()
        
    
    
    
    #User_Answer = input((question))

    

    #print(question[1])
    #print(User_Answer)
    
#Game_start()




# if __name__ == "Play_game.py":
#     main()

