import pygame
import game
import load

guesses = 0
guess = []
first_keys = True
last_keys = []

def setup():
    load.main()

def add_letter(letter):
    if len(guess) + 1 <= 5:
        load.load_letter(guesses, letter)
        guess.append(letter)
    
def remove_letter():
    load.remove_letter(guesses)
    guess.pop()

def keyboard_input():

    keys = pygame.key.get_pressed()        
    for i in range(len(keys)):
        if (keys[i] == True):
            key = str(chr(i))
            
            #print(len(key), key[0], key)
            key = key.upper()
            # Checking if the key pressed is a letter and if it is not already marked as absent
            if len(key) == 1 and key.isalpha() == True and len(guess) < 5 and load.keyboard_state[load.chr_int(key)] != 0:
                
                # Keeping count of the frequency of the numbers in order to change states on the keyboard
                load.frecv[ord(key) - ord('A')] += 1
                add_letter(key)
                #print("TRYING TO ADD")

            elif (i == 8 or i == 127) and len(guess) > 0 and guesses <= 5: # Pressing DELETE or BACKSPACE
                remove_letter()
            elif (i == 13) and len(guess) == 5 and guesses <= 5: # Pressing ENTER to guess
                word_guess()
            #print(f"{i} f{chr(i)}") 
    
def word_guess():
    
    global guess
    global guesses
    for i in range(5):
        print(str(guess[i]), str(game.word[i]))
        # Checking if the letter match
        if str(guess[i]) == str(game.word[i]):
            load.change_keyboard_state(i, 2)
            load.change_table_state(i, 2)
        # Checking if the letter is found anywhere in the word    
        elif game.word.find(guess[i]) != -1:
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

    if str_guess == game.word or guesses == 6:
        print("RUNNING IS SET TO FALSE")
        game.running = False
        return
    
    guess.clear()
       
                    
def main():
    setup()


if __name__ == "__main__":
    main()