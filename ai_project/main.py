
import pygame
import random

pygame.init()

BLACK = (0, 0 ,  0)
size = [600, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    # 이미지 로드
    background_image = pygame.image.load('bgbgbgbg.png')
    background_image = pygame.transform.scale(background_image, (600, 800))

    snowball_image = pygame.image.load('snow11.png')
    snowball_image = pygame.transform.scale(snowball_image, (50, 50))
    snowballs = []

    for i in range(5):
        rect = pygame.Rect(snowball_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        snowballs.append({'rect': rect, 'dy': dy})

    person_image = pygame.image.load('polar.png')
    person_image = pygame.transform.scale(person_image, (100, 100))
    person = pygame.Rect(person_image.get_rect())
    person.left = size[0] // 2 - person.width // 2
    person.top = size[1] - person.height
    person_dx = 0

    # 점수 관련 변수
    score = 0
    font = pygame.font.Font(None, 36)

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        # 배경 그리기
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    person_dx = -5
                elif event.key == pygame.K_RIGHT:
                    person_dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    person_dx = 0
                elif event.key == pygame.K_RIGHT:
                    person_dx = 0

        for snowball in snowballs:
            snowball['rect'].top += snowball['dy']
            if snowball['rect'].top > size[1]:
                snowballs.remove(snowball)
                rect = pygame.Rect(snowball_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                snowballs.append({'rect': rect, 'dy': dy})

        person.left = person.left + person_dx

        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width

        screen.blit(person_image, person)

        for snowball in snowballs:
            if snowball['rect'].colliderect(person):
                done = True  # 눈덩이와 충돌하면 게임 종료
            screen.blit(snowball_image, snowball['rect'])

        # 점수 업데이트 및 표시
        score += 1
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if score >= 2000:
            done = True

        pygame.display.update()

runGame()
pygame.quit()