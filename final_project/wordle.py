import pygame
import csv
import load
guesses = 0
guess = []
first_keys = True
last_keys = []

def setup():
    load.main()

def add_letter(letter):
    if len(guess) < 5:
        load.load_letter(guesses, letter)
        load.frecv[load.chr_int(letter)] += 1
        guess.append(letter)
    
def remove_letter():
    load.remove_letter(guesses)
    guess.pop()

def hard_mode_pass():
    for letter in load.letters:
        # Checking that all the letters marked with yellow or green are present in the current guess
        if load.keyboard_state[load.chr_int(letter)] == 2 or load.keyboard_state[load.chr_int(letter)] == 4:
            str_guess = str(guess)
            if str_guess.find(letter) == -1:
                return False
    return True

def keyboard_input(event, word):              
    # Pressing a letter
    if event.unicode and event.unicode.isalpha() and guesses <= 5:
        key = event.unicode.upper()
        add_letter(key)
    # Pressing backspace / delete
    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE: 
        if len(guess) > 0 and guesses <= 5:
            remove_letter()
    # Pressing enter
    elif event.key == pygame.K_RETURN: 
        if len(guess) == 5 and guesses <= 5 and word_check(guess):
            if load.hard_mode_state == 0 or (load.hard_mode_state == 1 and hard_mode_pass()):
                return word_guess(word)
    return False

def mouse_input(event):
    for letter in load.letters:
        curr_letter = load.keyboard[load.chr_int(letter)]

        # Creates a rectangel the size of the image
        img_rect = curr_letter[0].get_rect()

        # Places the rectangle in same position as the letter
        img_rect.topleft = (curr_letter[1], curr_letter[2])

        # Checks whether the mouse position is whithin the image's coordinates at the moment of clicking
        if img_rect.collidepoint(event.pos) and guesses <= 5:
            add_letter(letter)

    check_hard_mode(event)

def check_hard_mode(event):

    curr = load.hard_mode_button
    # Creates a rectangle the size of the image
    img_rect = curr[0].get_rect()
    
    # Places the rectangle in same position as the button
    img_rect.topleft = (curr[1], curr[2])

    if img_rect.collidepoint(event.pos) and guesses <= 5:
        # Changes the state of the button
        load.hard_mode_state = (1 - load.hard_mode_state) 

def word_check(wordd):

    str_wordd = ''.join(wordd).upper()
    with open("valid_words.csv", 'r', newline='\n') as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            for val in row.values():
                if val.upper() == str_wordd:
                    return True
    return False

def word_guess(word):


    global guess
    global guesses
    for i in range(5):
        print(str(guess[i]), str(word[i]))
        # Checking if the letter match
        if str(guess[i]) == str(word[i]):
            load.change_keyboard_state(i, 2)
            load.change_table_state(i, 2)
        # Checking if the letter is found anywhere in the word    
        elif word.find(guess[i]) != -1:
            if load.keyboard_state[load.chr_int(guess[i])] != 2:
                load.change_keyboard_state(i, 4)
            load.change_table_state(i, 4)
        # Stating that the letter is absent    
        else:
            load.change_table_state(i, 0)
            load.change_keyboard_state(i, 0)

    # Counting the number of guesses
    guesses += 1
    # Converting list to string 
    str_guess = ''.join(guess)
    # Checking whether the word guessed is the right one
    if str_guess == word or guesses == 6:
        #print("RUNNING IS SET TO FALSE")
        return True
    
    for i in range(len(load.frecv)):
        load.frecv[i] = 0
    guess.clear()
    return False
            
def main():
    setup()

if __name__ == "__main__":
    main()