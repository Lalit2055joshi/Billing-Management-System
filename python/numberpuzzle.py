from random import *
x = randint(1, 100) 

number_of_guess=0
def playgame(x):
    number_of_guess=0
    while number_of_guess <=5:
        guess = int(input("enter the number"))
        number_of_guess +=1 
        if guess > x:
            print("your guess is below the random number")
        
        if guess < x:
            print("your guess is above the random number")
        
        if guess == x:
             print("you win!!")
             a=input("DO you want to play again type 'yes' or 'no' ")
             if a == 'yes':
                playgame(x)
             else:
                print("thanks for playing game")
                break
        elif guess != x and number_of_guess ==5 :
            print("You Lose")
            a=input("DO you want to play again type 'yes' or 'no' ")
            if a == 'yes':
                playgame(x)
            else:
                print("thanks for playing game")
                break 

playgame(x)
# option = input("enter do you want play again type 'yes' or 'no ")
# print(option)
# if option == 'yes':
#     playgame(x)
    
# else:
#     print("Thanks for playing game")
