import random
letters=["r","p","s"]

def play():
    computer=" "
    print(computer)
    user_score=0
    user=""
    computer_score=0
    while user_score<3 or computer_score<3:
        computer=random.choice(letters)
        print(f"computer choice :{computer}")
        user=input("please enter 'r' or 'p' or 's'")
        if user=="r" and computer=="s":
            user_score+=1      
        if user=="p" and computer=="s":
            computer_score+=1
        if user=="p" and computer=="r":
            user_score+=1
        if user=="s" and computer=="r":
            computer_score=1
        if user=="r" and computer=="p":
            computer_score+=1     
        if user=="s" and computer=="p":
            user_score+=1 
        if user==computer:
            print("ok let's do it again")
        if user_score==3 or computer_score==3:
            if user_score==3:
                print("You win")
            elif computer_score==3:
                print('You lose')

            break

        print("user score:",user_score)
        print("computer score:",computer_score)
        print("--------------------------------")


    


         



  


play()

    

            
            

 

