import requests
import json
import sys
import random

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
    word = word.replace(' ', '') #for evaluation of score
    return word

def make_guess():
    current_guess = input('Guess a letter: ') 
    if current_guess.isalpha() == True:
        if len(current_guess) == 1:
            return current_guess
        else:
            full_word_confirmation = input('Do you want to guess the whole word?\n')
            possible_confirmations = ['y', 'yes', 'yeah', 'sure']
            if full_word_confirmation.lower() in possible_confirmations:
                return current_guess
            else:
                print('Yeah thats what I thought')
                return current_guess
    else:
        print('Babez do you know what a letter is? Try again..')
        return make_guess()

def play_game(word_letters_array):
    guessed_letters = []
    wrong_guessed_letters = '' 
    left_tries = 5
    while left_tries > 0:
        current_guess = make_guess()
        if len(current_guess) == 1:
            if current_guess in guessed_letters:
                print('You already guessed that girlie.')
            elif current_guess in wrong_guessed_letters:
                print('You literally already tried that.')
            else: 
                guessed_letters += current_guess
                if current_guess in word_letters_array:
                    current_guess_progress = display_word(guessed_letters, word_letters_array)
                    if current_guess_progress == ''.join(word_letters_array):
                        print('OMG SLAY U WIN')
                        break
                else:
                    left_tries -=1 
                    if left_tries == 0:
                        print('Oh noo, looks like ur a lil looser baby. U can always try again doe.')
                        break
                    else: 
                        guessed_letters.remove(current_guess)
                        wrong_guessed_letters += current_guess + ' '
                        wrong_answer_templates = ['Not this time :/', 'Yeah no, not really', 'Sorry, try again', 'Good guess, but wrong']
                    print(f"{random.choice(wrong_answer_templates)}\nLetters tried: {wrong_guessed_letters}" )
        else:
            if current_guess == ''.join(word_letters_array):
                print('OMG SLAY U WIN')
                break
            else:
                left_tries -=1 
                if left_tries == 0:
                    print('Oh noo, looks like ur a lil looser baby. U can always try again doe.')
                    break
                else:
                    print("That's just completely wrong...")

if __name__ == '__main__':
    word, letters_array = get_word()
    print(word)
    display_word([], letters_array) 
    play_game(letters_array)
