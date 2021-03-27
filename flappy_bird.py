import pygame
import sys 
pygame.init() 

# Basic Display Stuff
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Flappy Bird')
flappy_bird_icon = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Images\PikPng.com_flappy-bird-png_2737091.png')
flappy_bird_icon = pygame.transform.scale(flappy_bird_icon, (32, 32))
pygame.display.set_icon(flappy_bird_icon)

# Basic User Screen Stuff
def title(x, y):
    green = (0, 255, 0)
    title = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Images\Flappy_Logo.png')
    title = pygame.transform.scale(title, (200, 42))
    screen.blit(title, (x, y))

def background():
    start_pos_x = -5
    end_pos_x = -25
    bush_x = -5
    cloud_x = -10
    bush = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Images\clipart6119.png')
    bush = pygame.transform.scale(bush, (32, 32))
    cloud = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Images\Daco_1189537.png')
    cloud = pygame.transform.scale(cloud, (100, 50))
    screen.fill((0, 191, 255))
    pygame.draw.rect(screen, (219,209,180), (0, 490, 700, 300))
    for item in range(12):
        screen.blit(cloud, (cloud_x, 410))
        cloud_x += 50
    for item in range(31):
        screen.blit(bush, (bush_x, 445))
        bush_x += 20
    pygame.draw.rect(screen, ((50,205,50)), (0, 470, 700, 20))
    for item in range(40):
        start_pos_x += 30
        end_pos_x += 30
        pygame.draw.line(screen, ((144,238,144)), (start_pos_x, 470), (end_pos_x, 490), 14)

def play_button():
    pass # Create Button

def flappy_bird():
    game_running = True
    while game_running:
        screen.fill(((0,206,209)))
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
        title(195, 70) # Finish making title

        pygame.display.update() 

#if __name__ == "__main___":
main_menu()