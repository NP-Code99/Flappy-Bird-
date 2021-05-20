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
    title = pygame.transform.scale(title, (260, 82))
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

# Buttons
def play_button(x, y, length, width, color):
    play_button = (x, y, length, width)
    play_button_text = pygame.font.Font(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Fonts\game_over.ttf', 90).render('Start', True, (255, 255, 255)) 
    pygame.draw.rect(screen, color, play_button) 
    pygame.draw.rect(screen, (255, 255, 255), play_button, 3) 
    screen.blit(play_button_text, (x + 29, y))

# Flappy Bird Character 
def character(x, y):
    flappy_bird_character = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Images\PikPng.com_flappy-bird-png_2737091.png')
    flappy_bird_character = pygame.transform.scale(flappy_bird_character, (60, 40))
    screen.blit(flappy_bird_character, (x, y))

def flappy_bird():
    game_running = True
    character_y = 210
    character_y_rate = 100
    while game_running:
        background()
        character(265, character_y)
        score = 0
        score_text = pygame.font.Font(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Fonts\04B_19__.TTF', 50).render(str(score), True, (255, 255, 255))
        ready_text = pygame.font.Font(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Flappy-Bird-\All Fonts\game_over.ttf', 100).render('Get Ready', True, ((255,165,0)))
        character_y +=  5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                character_y -= character_y_rate
        if character_y < -200:
            character_y = 0
        elif character_y > 429:
            character_y = 429
        screen.blit(score_text, (280, 60))
        screen.blit(ready_text, (200, 120))
        pygame.display.update()

def main_menu():
    main_menu_running = True
    while main_menu_running:
        background()
        title(165, 40)
        play_button(222, 220, 150, 60, (255,140,0))
        character(265, 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y += 1 
                elif event.key == pygame.K_UP:
                    y -= 1
                elif event.key == pygame.K_LEFT:
                    x -= 1
                elif event.key == pygame.K_RIGHT: 
                    x += 1
                print(x, y)
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 221 and mouse_pos_x <= 372 and mouse_pos_y >= 217 and mouse_pos_y <= 279:
                    flappy_bird()
        pygame.display.update() 

#if __name__ == "__main___":
flappy_bird()