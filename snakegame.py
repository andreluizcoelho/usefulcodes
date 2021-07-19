
#This a snake game built using the pygame library. 
#This was built by the instructor https://github.com/gil-air-may from Kenzie Academy Brazil.
#During the free online week that I participated on the last week of April, 2021.
#Most variables were originally in Portuguese, I translated it to English.
#There's also a 'typingspeed.ipynb' game in this repository that he made and I adapted it, although it was not created with pygame library. 
#The typing speed time there is mine.

import pygame
import random


pygame.init()

blue = (50, 100, 213)
orange = (205, 102, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)


dimensions = (600, 600)

### Initial Values ###
x = 300
y = 300
d = 20

list_snake = [[x, y]]

dx = 0
dy = 0

x_food = round(random.randrange(0, 600 - d) / 20) * 20
y_food = round(random.randrange(0, 600 - d) / 20) * 20

font = pygame.font.SysFont("hack", 35)



screen = pygame.display.set_mode((dimensions))
pygame.display.set_caption('Snake from Kenzie')
screen.fill(blue)
clock = pygame.time.Clock()

def draw_snake(list_snake):
    screen.fill(blue)
    for unit in list_snake:
        pygame.draw.rect(screen, orange, [unit[0], unit[1], d, d])

def move_snake(dx, dy, list_snake):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_new = list_snake[-1][0] + dx
    y_new = list_snake[-1][1] + dy

    list_snake.append([x_new, y_new])
    del list_snake[0]
    return dx, dy, list_snake

def verify_food(dx, dy, x_food, y_food, list_snake):
    head = list_snake[-1]
    x_new = head[0] + dx
    y_new = head[1] + dy

    if head[0] == x_food and head[1] == y_food:
        list_snake.append([x_new, y_new])
        x_food = round(random.randrange(0, 600 - d) / 20) * 20
        y_food = round(random.randrange(0, 600 - d) / 20) * 20



    pygame.draw.rect(screen, green, [x_food, y_food, d, d])


    return x_food, y_food, list_snake

def verify_wall(list_snake):
    head = list_snake[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        raise Exception 

def verify_bit_snake(list_snake):
    head = list_snake[-1]
    body = list_snake.copy()


    del body[-1]
    for x,y in body: 
        if x == head[0] and y == head[1]:
            raise Exception

def update_points(list_snake):
    pts = str(len(list_snake))
    score = font.render("Points: " + pts, True, yellow)
    screen.blit(score,[0,0])

while True:
    pygame.display.update()
    draw_snake(list_snake)
    dx, dy, list_snake = move_snake(dx, dy, list_snake)
    x_food, y_food, list_snake = verify_food(
        dx, dy, x_food, y_food, list_snake)
    print(list_snake)
    verify_wall(list_snake)
    verify_bit_snake(list_snake)
    update_points(list_snake)

    clock.tick(10)
    