import pygame
import wordle
pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
running = True
word = str
word = "horse"
def pygame_setup():
    global running
    while running == True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                wordle.keyboard_input()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((42, 44, 56))
        wordle.main()
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()   
def main():
    pygame_setup()

if __name__ == "__main__":
    main()