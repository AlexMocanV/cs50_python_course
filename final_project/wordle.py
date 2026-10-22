import pygame
import game
import load
def main():
    
    rect = pygame.Rect(0, 0, 10, 20)
    pygame.draw.rect(game.screen, (0, 255, 0), rect)
    load.main()

if __name__ == "__main__":
    main()