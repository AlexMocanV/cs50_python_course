import pygame
import wordle
import game

# keyboard
states_name = ["absent_", "selected_", "correct_", "default_", "present_"]
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
textures = {}

all_textures = []
keyboard_state = []
frecv = []

loaded_keyboard = False
loaded_table_of_guesses = False
# table of guesses
table_of_words_guessed = []
blank = 0

def loading_keyboard():
    i = 0
    for letter in letters:
        # set state to default
        new_list = []
        all_textures.append(new_list)
        keyboard_state.append(3)
        frecv.append(0)

    for i in range(5):
        for letter in letters:
            path = ".\\letters_textures\\" + states_name[i] + letter + '.png'
            img = pygame.image.load(path)

            # Scaled the letter so they are scaled with the rezolution
            img = pygame.transform.scale(img, (game.screen.get_height() / 12, game.screen.get_height() / 12))

            all_textures[ord(letter) - ord('A')].append(img)
            if i == 3:
                textures[letter] = img
                
        
    global loaded_keyboard
    loaded_keyboard = True

# Displaying the keyboard
def display_keyboard():
    # Displaying the default keyboard
    global loaded_keyboard
    if loaded_keyboard == False:
        loading_keyboard()
        loaded_keyboard = True
    
    # x is calculated, so the keyboard is in the middle of the screen horrizontally
    native_x = (game.screen.get_width() - textures["A"].get_width() * 10 - 10 * (textures["A"].get_width() / 12)) / 2    
    x = native_x

    # y is calculated so the keyboard is in the bottom of the screen
    native_y = int(game.screen.get_height() / 1.5)
    y = native_y

    cnt = 0
    for letter in letters:
        textures[letter] = all_textures[ord(letter) - ord('A')][keyboard_state[ord(letter) - ord('A')]]
        game.screen.blit(textures[letter], (x, y))
        if letter == "P" or letter == "L":
            # Modifing the positions to have a bit of space between the letters 
            # And to have the wordle like shape
            cnt += 1
            x = native_x + (textures[letter].get_width() + (textures[letter].get_width() / 12)) / 2 * cnt
            y = native_y + cnt * (textures[letter].get_height() + (textures[letter].get_width() / 12))
        else: 
            x += (textures[letter].get_width() + (textures[letter].get_width() / 12))

def load_table_of_guesses():

    # Drawing a table out of simple empty buttons

    path = ".\\letters_textures\\default_blank.png"
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (game.screen.get_height() / 12, game.screen.get_height() / 12))
    global blank
    blank = img

    # Designed the table so that it is scaled with the rezolution
    _ = 0
    i = 0
    native_x = (game.screen.get_width() - img.get_width() * 5 - 5 * (img.get_width() / 12)) / 2    
    x = native_x

    native_y = img.get_height()
    y = native_y
    
    for _ in range(6):
        words_guessed = []
        for i in range(5):
            words_guessed.append((img, x, y))
            x = x + img.get_width() + img.get_width() / 12
        table_of_words_guessed.append(words_guessed)
        x = native_x
        y = y + img.get_height() + img.get_height() / 12

def display_table_of_guesses():
    # Loading the default table
    global loaded_table_of_guesses
    if loaded_table_of_guesses == False:
        load_table_of_guesses()
        loaded_table_of_guesses = True

    # Updating the table
    for i in range(6):
        for j in range(5):
            curr_img = table_of_words_guessed[i][j]
            game.screen.blit(curr_img[0], (curr_img[1], curr_img[2]))

def load_letter(guesses, letter):

    letter = letter.upper()
    
    # Loading the default texture
    new_texture = all_textures[ord(letter) - ord('A')][3] 
    
    # Changing the keyboard state to selected
    keyboard_state[ord(letter) - ord('A')] = 1

    # Changing the table's state back to default
    curr_data = table_of_words_guessed[guesses][len(wordle.guess)]
    table_of_words_guessed[guesses][len(wordle.guess)] = (
        new_texture,
        curr_data[1],
        curr_data[2]
    )
def remove_letter(guesses):
    
    curr_data = table_of_words_guessed[guesses][len(wordle.guess) - 1]

    # Changing the selected state back to default 
    # if after the letters removal there are no more appereances in the string
    
    last_letter = wordle.guess[len(wordle.guess) - 1]
    
    if frecv[ord(last_letter) - ord('A')] - 1 <= 0:
        keyboard_state[ord(last_letter) - ord('A')] = 3

    frecv[ord(last_letter) - ord('A')] -= 1
    
    # Changing the table's state back to default
    table_of_words_guessed[guesses][len(wordle.guess) - 1] = (
        blank,
        curr_data[1],
        curr_data[2]
    )

def change_state(index, state):
    
    letter = ord(wordle.guess[index]) - ord('A')

    #Changing the state on the keyboard
    keyboard_state[letter] = state

    #Changing the state on the Word Table
    
    new_texture = all_textures[letter][state]
    curr_data = table_of_words_guessed[wordle.guesses][index]

    table_of_words_guessed[wordle.guesses][index] = (
        new_texture,
        curr_data[1],
        curr_data[2]
    )

def main():
    display_keyboard()
    display_table_of_guesses()

if __name__ == "__main__":
    main()