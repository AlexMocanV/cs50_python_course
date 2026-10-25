import pygame
import game
import load
guesses = 0
guess = []
def setup():
    rect = pygame.Rect(0, 0, 10, 20)
    pygame.draw.rect(game.screen, (0, 255, 0), rect)
    load.main()

def add_letter(letter):
    if len(guess) == 0:
        load.load_letter(guesses, letter)
        guess.append(letter)
    elif len(guess) + 1 <= 5:
        load.load_letter(guesses, letter)
        guess.append(letter)
    if len(guess) > 4:
        print(guess[4])
def remove_letter():
    load.remove_letter(guesses)
    guess.pop()

def keyboard_input():
    keys = pygame.key.get_pressed()
    i = 0
    for i in range(len(keys)):
        if (keys[i] == True):
            key = str(chr(i))
            #print(len(key), key[0], key)   
            if len(key) == 1 and key.isalpha() == True and len(guess) < 5:
                key = key.upper()
                load.frecv[ord(key) - ord('A')] += 1
                add_letter(key)
                #print("TRYING TO ADD")
            elif (i == 8 or i == 127) and len(guess) > 0: # pressing DELETE or BACKSPACE
                remove_letter()
            elif (i == 13) and len(guess) == 5: # pressing ENTER
                word_guess()
            #print(f"{i} f{chr(i)}") 
def word_guess():
    global guess
    global guesses
    print(guess)
    for i in range(5):
        print(i)
        if str(guess[i]) == str(game.word[i]):
            load.change_state(i, 2)
        elif game.word.find(guess[i]) != -1:
            load.change_state(i, 4)
        else:
            load.change_state(i, 0)
    guesses += 1
    guess.clear()
       
                    
def main():
    setup()


if __name__ == "__main__":
    main()