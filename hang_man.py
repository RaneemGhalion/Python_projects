"""The hangman game is a multiplayer game. In this game, one player selects a word. 
Other players have a certain number of guesses to guess the characters in the word. 
If the players are able to guess the
 characters in the entire word within certain attempts, they win. Otherwise, they lose."""

from words import words
import random
import string


def get_valid_word(words):
    word=random.choice(words)

    while "-" in word or " " in word:
        word=random.choice(words)
    print("---word-----",word)
    the_word_letters_list=[]    
    # make the letters as a list
    for letter in word:
        the_word_letters_list.append(letter)

    return the_word_letters_list

    
  




def get_the_word():
    the_word_letters_list=get_valid_word(words)
    # tell the user the length of the word
    print(len(the_word_letters_list))
    hangman(the_word_letters_list)


def hangman(the_word_letters_list):
    the_guess=input("please enter a guess")
    handel_user_input(the_guess)
    check_if_guess_in_the_word(the_word_letters_list,the_guess)

def handel_user_input(the_guess):
    guess_letters=[]
    # check that the input is from the alphabet
    alphabet=set(string.ascii_lowercase)
    if  the_guess in alphabet:
        guess_letters.append(the_guess)
    else:
        print("unvalid input")



    # check if the guess is in the word
def check_if_guess_in_the_word(the_word_letters_list,the_guess):

    while the_guess in the_word_letters_list:
        the_word_letters_list.remove(the_guess)
        print(the_word_letters_list)
        if len(the_word_letters_list)==0:
            print("Congrats You Won!")
            print("finish") 

            break
        the_guess=input("please enter another guess")
        handel_user_input(the_guess)
        check_if_guess_not_in_the_word(the_guess,the_word_letters_list)


        
def check_if_guess_not_in_the_word(the_guess,the_word_letters_list): 

    while the_guess not in the_word_letters_list:
        print("try again")
        # check_if_guess_in_the_word(the_word_letters_list,the_guess)
        hangman(the_word_letters_list)
        break





get_the_word()    