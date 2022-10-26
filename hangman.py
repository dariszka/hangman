
from curses.ascii import isalpha
import requests
import json
import sys

response = requests.get("https://random-word-api.herokuapp.com/word")

def get_word():
    if response.status_code == requests.codes.ok:
        word = json.loads(response.text)[0]

        letters_array = []
        for letter in word:
            letters_array += letter

        return word, letters_array
    else:
        sys.exit("Error:", response.status_code, response.text) 

def display_word(guessed_letters_array, word_letters_array):
    word = ''
    for letter in word_letters_array:
        if letter in guessed_letters_array:
            word += letter + ' '
        else:
            word += '- '
    print(word)

def make_guess():
    current_guess = input('Guess a letter: ') 
    if current_guess.isalpha() == True:
        if len(current_guess) == 1:
            return current_guess
        else:
            print('Just one letter b.')
            make_guess()
    else:
        print('Babez do you know what a letter is? Try again..')
        make_guess()

# def check_for_letter(current_guess, guessed_letters_array, word_letters_array):
#     if current_guess in word_letters_array:
#         display_word(guessed_letters_array, word_letters_array)
#         return True 
#     else:
#         return False # to remove tries later

def play_game(word_letters_array):
    guessed_letters_array = [] #to display guessed letters l8r
    left_tries = 3
    while left_tries > 0:
        guessed_letter = make_guess()
        guessed_letters_array += guessed_letter
        # check_for_letter(guessed_letter, guessed_letters_array, word_letters_array)
        if guessed_letter in word_letters_array:
            display_word(guessed_letters_array, word_letters_array)
        else:
            left_tries -=1 

if __name__ == '__main__':
    word, letters_array = get_word()
    print(word)
    display_word([], letters_array) 
    play_game(letters_array)
