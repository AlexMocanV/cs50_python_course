import pygame
import wordle
import game

# keyboard
states_name = ["absent_", "selected_", "correct_", "default_", "present_"]
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"

all_textures = []
keyboard_state = []
frecv = []
hard_mode_button = 0
hard_mode_buttons_texture = []
keyboard = []

loaded_keyboard = False
loaded_table_of_guesses = False
loaded_hard_mode_button = False

hard_mode_state = False
# table of guesses
table_of_words_guessed = []
blank = 0
def chr_int(a) -> int:
    return ord(a) - ord('A')

def load_hard_mode():

    global hard_mode_button
    global loaded_hard_mode_button
    # Resized the buttons to be the same width as a letter    

    # Hard Mode OF button
    path_of_button = "hard_mode_of_button.png"
    
    img_of = pygame.image.load(path_of_button)
    
    img_of = pygame.transform.scale(img_of, (game.screen.get_height() / 12, game.screen.get_height() / 21))
    
    # Hard Mode ON button 
    path_on_button = "hard_mode_on_button.png"
    
    img_on = pygame.image.load(path_on_button)

    img_on = pygame.transform.scale(img_on, (game.screen.get_height() / 12, game.screen.get_height() / 21))

    # Setting the positon of the buttons
    distance_to_the_first_letter = (game.screen.get_width() - keyboard[0][0].get_width() * 10 - 10 * (keyboard[0][0].get_width() / 12)) / 2
        
    distance_to_halfway_of_first_letter = int(game.screen.get_height() / 1.5) + (keyboard[0][0].get_height()) / 4
    
    x, y = ((game.screen.get_width() - distance_to_the_first_letter) + 2 * keyboard[0][0].get_width(), distance_to_halfway_of_first_letter + keyboard[0][0].get_height())
        
    hard_mode_buttons_texture.append(img_of) 
    hard_mode_buttons_texture.append(img_on) 
    hard_mode_button = (img_of, x, y)

    loaded_hard_mode_button = True


def display_hard_mode():

    global hard_mode_button
    global loaded_hard_mode_button

    if loaded_hard_mode_button == False:
        load_hard_mode()

    img, x, y = hard_mode_button
    hard_mode_button = (hard_mode_buttons_texture[hard_mode_state], x, y)
    game.screen.blit(hard_mode_buttons_texture[hard_mode_state], (x, y))

def loading_keyboard():
    
    for letter in letters:
        # Set state to default, appeareaces to each letter to 0, preprare the texture list of list
        new_list = []
        all_textures.append(new_list)
        keyboard_state.append(3)
        keyboard.append(0)
        frecv.append(0)

    for i in range(5):
        for letter in letters:
            path = ".\\letters_textures\\" + states_name[i] + letter + '.png'
            img = pygame.image.load(path)

            # Scaled the letter so they are scaled with the rezolution
            img = pygame.transform.scale(img, (game.screen.get_height() / 12, game.screen.get_height() / 12))

            # Saved all textures in a list of list
            all_textures[chr_int(letter)].append(img)
            if i == 3:
                keyboard_state[chr_int(letter)] = 3
                
        
    global loaded_keyboard
    loaded_keyboard = True

    # x is calculated, so the keyboard is in the middle of the screen horrizontally
    native_x = (game.screen.get_width() - game.screen.get_height() / 12 * 10 - 10 * (game.screen.get_height() / 12 / 12)) / 2    
    x = native_x

    # y is calculated so the keyboard is in the bottom of the screen
    native_y = int(game.screen.get_height() / 1.5)
    y = native_y

    cnt = 0
    for letter in letters:
        img = all_textures[chr_int(letter)][keyboard_state[chr_int(letter)]]
        keyboard[chr_int(letter)] = (img, x, y)
        if letter == "P" or letter == "L":
            # Modifing the positions to have a bit of space between the letters 
            # And to have the wordle like shape
            cnt += 1
            x = native_x + (img.get_width() + (img.get_width() / 12)) / 2 * cnt
            y = native_y + cnt * (img.get_height() + (img.get_width() / 12))
        else: 
            x += (img.get_width() + (img.get_width() / 12))

def display_keyboard():
    # Displaying the default keyboard
    global loaded_keyboard
    if loaded_keyboard == False:
        loading_keyboard()
        loaded_keyboard = True
        return
    
    for letter in letters:
        curr_letter = keyboard[chr_int(letter)]
        keyboard[chr_int(letter)] = (
            all_textures[chr_int(letter)][keyboard_state[chr_int(letter)]], 
            curr_letter[1], 
            curr_letter[2]
        )
        game.screen.blit(curr_letter[0], (curr_letter[1], curr_letter[2]))
    

def load_table_of_guesses():

    # Drawing a table out of simple empty / blank buttons

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
    new_texture = all_textures[chr_int(letter)][3] 
    
    # Changing the keyboard state to selected if its blank
    if keyboard_state[chr_int(letter)] == 3:
        keyboard_state[chr_int(letter)] = 1

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
    # if after the letters removal there are no more appereances of the same letter in the string
    last_letter = wordle.guess[len(wordle.guess) - 1]
    frecv[chr_int(last_letter)] -= 1
    
    # Only reset keyboard state back to default (3) if it was currently selected (1).
    if frecv[chr_int(last_letter)] <= 0:
        if keyboard_state[chr_int(last_letter)] == 1:
            keyboard_state[chr_int(last_letter)] = 3
    
    # Changing the table's state back to default
    table_of_words_guessed[guesses][len(wordle.guess) - 1] = (
        blank,
        curr_data[1],
        curr_data[2]
    )

def change_keyboard_state(index, state):
    
    letter = ord(wordle.guess[index]) - ord('A')

    # Changing the state of the keyboard
    keyboard_state[letter] = state

def change_table_state(index, state):
    
    # Changing the state of the Word Table
    letter = ord(wordle.guess[index]) - ord('A')
    
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
    # Always call display_keyboard before display_hard_mode because otherwise keyboard[][] won't be initiliazed
    display_hard_mode()

if __name__ == "__main__":
    main()