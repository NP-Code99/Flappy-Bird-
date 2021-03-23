import pygame
import sys 
pygame.init() 

# Basic Stuff
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Flappy Bird')
bird_icon = pygame.image.load(r'C:\Users\Admin\Downloads\hummingbird.png')
pygame.display.set_icon(bird_icon)

def flappy_bird():
    game_running = True
    while game_running:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

def main_menu():
    main_menu_running = True
    while main_menu_running:
        screen.fill((0, 0, 205))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
        screen.blit(pygame.font.SysFont('impact', 20).render('Flappy Bird', True, (0, 0, 0))) # Finish making title
        pygame.display.update() 

#if __name__ == "__main___":
main_menu()