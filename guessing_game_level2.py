import random
def computer_guess(x):
    low=1
    high=x
    guess=0
    # the computer suggest a number 
    # print(f"the number is {guess}")
    # the user would say yes or no 
    result="N"
    print("let me try ")
    guess=random.randint(low,high)
    print(guess)
    result=input("is it too high or too low (Y/N)? : ").upper()
    while result=="HIGH":
        guess-=1
        print (guess)
        result=input("is it too high or too low (Y/N)?").upper()
    while result=="LOW":
        guess+=1
        print(guess)
        result=input("is it too high or too low (Y/N)?").upper()
    if result=="Y"or "y":
        print("WOW I DID IT")


        

    



    # if user said yes print Hay! 
    # if the user said no try again



computer_guess(10)