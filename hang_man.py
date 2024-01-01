"""The hangman game is a multiplayer game. In this game, one player selects a word. 
Other players have a certain number of guesses to guess the characters in the word. 
If the players are able to guess the
 characters in the entire word within certain attempts, they win. Otherwise, they lose."""


"""adding conditons :
when the user pick a letter and it exists in more than one place it should delete them both (done)
only five wrong times + the letters number
"""

from words import words
import random
import string
# global attempts
the_word_letters_list=set()   


attempts=0
def handel_attempts(the_word_letters_list):
    global attempts
    if attempts==0:
        attempts=len(the_word_letters_list)+4
 
    else:
        attempts=attempts-1
    print("You have ",attempts," attempts")
    return attempts


def get_valid_word(words):
    word=random.choice(words)
    print("attempts",attempts)

    while "-" in word or " " in word:
        word=random.choice(words)
    print("---word-----",word)
    # make the letters as a list
    for letter in word:
        the_word_letters_list.add(letter)

    return the_word_letters_list

    
  




def get_the_word():
    the_word_letters_list=get_valid_word(words)
    # tell the user the length of the word
    print(len(the_word_letters_list))
    print("len(the_word_letters_list)",len(the_word_letters_list))
    hangman(the_word_letters_list)



    
    

def hangman(the_word_letters_list):
    the_guess=input("please enter a guess")
    handel_user_input(the_guess,the_word_letters_list)
    check_if_guess_in_the_word(the_word_letters_list,the_guess)




def handel_user_input(the_guess,the_word_letters_list):
    # print("handel_user_input")
    guess_letters=[]
    # check that the input is from the alphabet
    alphabet=set(string.ascii_lowercase)
    if  the_guess in alphabet:
        guess_letters.append(the_guess)
    else:
        print("unvalid input")
        hangman(the_word_letters_list)



    # check if the guess is in the word
def check_if_guess_in_the_word(the_word_letters_list,the_guess):
    # print("check_if_guess_in_the_word")
    # print("---------------------------")


    while the_guess in the_word_letters_list:
        attempts_result=handel_attempts(the_word_letters_list)
        if attempts_result==0:
            print("You lose")
            break

        the_word_letters_list.remove(the_guess)
        # handel_attempts(the_word_letters_list)
        print(the_word_letters_list)
        print("len ",len(the_word_letters_list))
        if len(the_word_letters_list)==0:
            print("Congrats You Won!")
            # print("finish") 
            break
    else:
        
        check_if_guess_not_in_the_word(the_guess,the_word_letters_list)


        
def check_if_guess_not_in_the_word(the_guess,the_word_letters_list): 
    # print("check_if_guess_not_in_the_word")
    attempts_result=handel_attempts(the_word_letters_list)
 

    while the_guess not in the_word_letters_list:
        if attempts_result==0:
            print("You lose")

            break
        print("try again")
        # check_if_guess_in_the_word(the_word_letters_list,the_guess)
        # attepts_fun(the_word_letters_list)
        hangman(the_word_letters_list)
        break





get_the_word()    