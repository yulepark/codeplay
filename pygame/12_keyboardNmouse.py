import pygame
import random
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("sniper sansu game")

circleX_pos = 0
circleY_pos = 0

sound_a = pygame.mixer.Sound("pygame/source/Car Horn.wav")
sound_b = pygame.mixer.Sound("pygame/source/Alert.wav")
sound_c = pygame.mixer.Sound("pygame/source/야옹.wav") 


clock = pygame.time.Clock()

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height

character_to_x = 0
character_to_y = 0

enemy = pygame.image.load("pygame/source/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = (screen_width / 2 - enemy_width / 2)
enemy_yPos = screen_height - enemy_height

enemy_to_x = 0
enemy_to_y = 0

ball = pygame.image.load("pygame/source/ball.png")
ball_size = character.get_rect().size
ball_width = character_size[0]
ball_height = character_size[1]
ball_xPos = (screen_width / 2 - ball_width / 2)
ball_yPos = screen_height - ball_height

ball_speed_x = 3
ball_speed_y = 3

running = True
while running:
    dt = clock.tick(60)

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

        mouseX_pos = 0
        mouseY_pos = 0
        if event.type == pygame.MOUSEMOTION:
            mouse_Pos = pygame.mouse.get_pos()
            mouseX_pos = mouse_Pos[0]
            mouseY_pos = mouse_Pos[1]

        character_xPos += character_to_x * dt
        character_yPos += character_to_y * dt

        if character_xPos < 0:
            character_xPos = 0
        elif character_xPos > screen_width - character_width:
            character_xPos = screen_width - character_width
        if character_yPos < 0:
            character_yPos = 0
        elif character_yPos > screen_height - character_height:
            character_yPos = screen_height - character_height

        if enemy_xPos < 0:
            enemy_xPos = 0
        elif enemy_xPos > screen_width - enemy_width:
            enemy_xPos = screen_width - enemy_width
        if enemy_yPos < 0:
            enemy_yPos = 0
        elif enemy_yPos > screen_height - enemy_height:
            enemy_yPos = screen_height - enemy_height

    ball_xPos += ball_speed_x
    ball_yPos += ball_speed_y

    if ball_xPos <= 0:
        ball_speed_x *= -1
        ball_speed_x = -random.randint(3, 8)

    elif ball_xPos >= screen_width - ball_width:
        ball_speed_x *= -1
        ball_speed_x = -random.randint(3, 8)

    if ball_yPos <= 0:
        ball_speed_y *= -1
        ball_speed_y = random.randint(3, 8)

    elif ball_yPos >= screen_height - ball_height:
        ball_speed_y *= -1
        ball_speed_y = random.randint(3, 8)

        screen.fill((255,255, 255))
        screen.blit(character, (character_xPos, character_yPos))
        screen.blit(enemy, (enemy_xPos, enemy_yPos))
        screen.blit(ball, (ball_xPos, ball_yPos))
        pygame.display.update()



pygame.quit()