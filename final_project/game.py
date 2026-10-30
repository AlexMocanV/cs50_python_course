import random
import sys
import pygame
import wordle
import load
import csv

pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
running = True
reader = {}
def get_random_word():

    with open("valid_solutions.csv", 'r', newline='\n') as input_file:
        reader = csv.DictReader(input_file)
        rows = list(reader)
        if rows:
            # Extract the actual word string from the dictionary row
            row_dict = random.choice(rows)
            word = list(row_dict.values())[0].upper()
            return word
    return "HORSE"

word = ""
def pygame_setup():
    global running
    while running == True:
        # poll for events
        for event in pygame.event.get():
            if running == False:
                break
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                else:
                    if wordle.keyboard_input(event, word):
                        running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for left click only
                if event.button == 1:
                    wordle.mouse_input(event)
        # fill the screen with a color to wipe away anything from last frame
        screen.fill((42, 44, 56))
        wordle.main()
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(144)  # limits FPS to 144

    print("QUIT")  

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
    pygame.quit()

def main():
    global word 
    word = get_random_word()
    print(word)
    pygame_setup()

if __name__ == "__main__":
    main()
    