import pygame
import wordle
import game

def loading_keyboard():
    # Loading the textures from the folder

    states_name = ["absent_", "default_", "correct_", "default_"]
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    textures = {}
    i = 0

    for i in range(4):
        for letter in letters:
            path = ".\\letters_textures\\" + states_name[i] + letter + '.png'
            img = pygame.image.load(path)

            # Scaled the letter so they are scaled with the rezolution
            img = pygame.transform.scale(img, (game.screen.get_height() / 12, game.screen.get_height() / 12))
            textures[letter] = img
    
    # Displaying the keyboard

    # x is calculated, so the keyboard is in the middle of the screen horrizontally
    native_x = (game.screen.get_width() - textures["A"].get_width() * 10 - 10 * (textures["A"].get_width() / 12)) / 2    
    x = native_x

    # y is calculated so the keyboard is in the bottom of the screen
    native_y = int(game.screen.get_height() / 1.5)
    y = native_y

    cnt = 0
    for letter in letters:
        game.screen.blit(textures[letter], (x, y))
        if letter == "P" or letter == "L":
            # Modifyg the positions to have a bit of space between the letters 
            # And to have the wordle like shape
            cnt += 1
            x = native_x + (textures[letter].get_width() + (textures[letter].get_width() / 12)) / 2 * cnt
            y = native_y + cnt * (textures[letter].get_height() + (textures[letter].get_width() / 12))
        else: 
            x += (textures[letter].get_width() + (textures[letter].get_width() / 12))
def load_word_table():

    # Drawing a table out of simple empty buttons
    path = ".\\letters_textures\\default_blank.png"
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (game.screen.get_height() / 12, game.screen.get_height() / 12))

    # Designed the table so that it is scaled with the rezolution
    _ = 1
    i = 1
    table_of_words = []
    words = []
    native_x = (game.screen.get_width() - img.get_width() * 5 - 5 * (img.get_width() / 12)) / 2    
    x = native_x

    native_y = img.get_height()
    y = native_y
    
    for _ in range(6):
        for i in range(5):
            game.screen.blit(img, (x, y))
            words.append({img, (x, y)})
            x = x + img.get_width() + img.get_width() / 12
        table_of_words.append(words)
        x = native_x
        y = y + img.get_height() + img.get_height() / 12
        

def main():
    loading_keyboard()
    load_word_table()

if __name__ == "__main__":
    main()