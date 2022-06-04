import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("명사수의 총알피하기-코플")

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            print("mouseMotion")
            print(pygame.mouse.get_pos())
            circleX_pos, circleY_pos = pygame.mouse.get_pos()
            screen.fill((11, 55, 26))
            pygame.draw.circle(screen, (255, 0 ,255), (circleX_pos, circleY_pos), 10)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("you pressed 정상수")
            print(pygame.mouse.get_pos())
            print(event.button)
            if event.button == 1:
                print("좌클")
            elif event.button == 3:
                print("우클")
            elif event.button == 2:
                print("휠클")
            elif event.button == 4:
                print("휠업")
            elif event.button == 5:
                print("휠다운")

        if event.type == pygame.MOUSEBUTTONUP:
            print("mouseButtonUp")
            pass

    pygame.display.update()


pygame.quit()