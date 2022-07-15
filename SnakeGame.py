from operator import imod
import pygame
##import package
import time
import random

# basic setup
snake_speed = 15

# window size
window_x = 720
window_y = 480

#defind color
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#initialize the game
pygame.init()

#initialize the game window
pygame.display.set_caption('Sanke Game')
game_window = pygame.display.set_mode((window_x, window_y))

#FPS
fps = pygame.time.Clock()

#snake initial position
snake_position = [100, 50]

#snake body
snake_body = [ [100, 50],
                [90, 50],
                [80, 50],
                [70, 50] ]

#fruit posiiton
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

#set default direction of snake to be right
direction = 'RIGHT'
change_to = direction

#initial score
score = 0

# show score function
def show_score(choice, color, font, size):
    #score font
    score_font = pygame.font.SysFont(font, size)
    #display object of score
    score_surface = score_font.render('Score : ' + str(score), True, color)
    #matrix object
    score_rect = score_surface.get_rect()
    #display text
    game_window.blit(score_surface,score_rect)

#game termination
def game_over():
    
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    #position
    game_over_rect.midtop = (window_x/2, window_y/4)
    #display on the screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    #time to exit
    time.sleep(2)
    #exit
    pygame.quit()
    quit()
    
#main program:

while True:
    
    #keyboard deal
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    # cant move to two different direction at same time
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    #snake move
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
        
    #snake grow,if clash with fruit, point+10
    snake_body.insert(0, list(snake_position))
    
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                        random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
        pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, white, pygame.Rect(
    fruit_position[0], fruit_position[1], 10, 10))
    
    #game over condition
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
        
    #touch the body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            
    #show consecutive scores
    show_score(1, white, 'times new roman', 20)
    
    #refresh the display
    pygame.display.update()
    #refresh rate
    fps.tick(snake_speed)