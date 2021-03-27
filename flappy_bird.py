import pygame
import sys 
pygame.init() 

# Basic Display Stuff
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Flappy Bird')
flappy_bird_icon = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Images\PikPng.com_flappy-bird-png_2737091.png')
flappy_bird_icon = pygame.transform.scale(flappy_bird_icon, (32, 32))
pygame.display.set_icon(flappy_bird_icon)

# Basic User Screen Stuff
def title(x, y, size):
    green = (0, 255, 0)
    title = pygame.font.Font(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Fonts\Youtube Star.TTF', size)
    screen.blit(title.render('Flappy Bird', True, green), (x, y))

def background():
    pass

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
        background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
        title(100, 100, 40) # Finish making title
        pygame.display.update() 

#if __name__ == "__main___":
main_menu()