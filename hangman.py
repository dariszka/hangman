
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

def display_word(letters_array):
    for letter in letters_array:
        print('-', end=' ')
    print('') #adds newline after word

def make_guess():
    guessed_letters = []
    guessed_letters = ''
    current_guess = input('Guess a letter: ') 
    if current_guess.isalpha() ==True:
        if len(current_guess) == 1:
            guessed_letters += current_guess
            return guessed_letters 
        else:
            print('Just one letter b.')
            make_guess()
    else:
        print('Babez do you know what a letter is? Try again..')
        make_guess()

def check_for_letter(current_guess, letters_array): 
    for letter in letters_array:
        if letter == current_guess:
            print(letter, end=' ')
        else:
            print('-', end=' ')
    print('')

if __name__ == '__main__':
    word, letters_array = get_word()
    print(word)
    display_word(letters_array)
    guessed_letter = make_guess()
    check_for_letter(guessed_letter, letters_array)

