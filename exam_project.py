import pygame
import random
import math


User_points = 0

def main():



    def Game_start():
        User_points = 0

    
        def Question_maker():
            
            List_of_numbers = ['1','2','3','4','5','6','7','8','9','10']
            
            List_of_operators = ['+','-','*','/']
            
            
            number1 = List_of_numbers[random.randint(0,9)]
            operand = List_of_operators[random.randint(0,3)]
            number2 = List_of_numbers[random.randint(0,9)]
            
            
            
            #Question = List_of_numbers[random.randint(0,9)] + list_of_operators[random.randint(0,3)] + List_of_numbers[random.randint(0,9)]
            
            Question = number1+operand+number2
            #Question = '10/3'
            
            
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
            

            
            
            
            
        question, answer = Question_maker()
        
        
        #print(question, answer)
        def Answer_checking():
            
            User_answer = input('Answer > ')
            
            if float(User_answer) == (answer)
            
            pass
            
        
        
        #User_Answer = input((question))

        

        #print(question[1])
        #print(User_Answer)
    
    Game_start()





if __name__ == "__main__":
    main()

