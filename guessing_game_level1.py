import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess<random_number:
            print("the number is more")
        if guess>random_number:
          print("the number is less")
    print("You win!")



guess(10)
