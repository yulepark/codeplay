# -*- coding: utf-8 -*-
from calendar import c
from operator import truediv
from random import random
import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("명사수의 총알피하기-코플")

clock = pygame.time.Clock()

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = random.randint(0, (screen_width - character_width))  
character_yPos = screen_height - character_height

to_x = 0 
to_y = 0
character_speed = 10        

enemy = pygame.image.load("pygame/source/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = random.randint(0, (screen_width - enemy_width))  
enemy_yPos = screen_height - enemy_height
enemy_speed = 10

to_x = 0 
to_y = 0



running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_xPos += to_x
    character_yPos += to_y

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    character_rect = enemy.get_rect()
    character_rect.left = enemy_xPos
    character_rect.top = enemy_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos 

    if character_rect.colliderect(enemy_rect):
        print("감전, 감전")
        running =False

    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))

    pygame.display.update()

    pygame.time.delay(2000)


pygame.quit()