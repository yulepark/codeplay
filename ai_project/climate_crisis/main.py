import pygame
import random

# Pygame 초기화
pygame.init()

# 창 설정
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("북극곰 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 배경 이미지 로드
background = pygame.image.load("ai_project\climate_crisis\main.bg.png")  # 배경 이미지 파일명을 적절히 변경하세요.

# 북극곰 이미지 로드
polar_bear = pygame.image.load("ai_project\climate_crisis\polar_bear.png")  # 북극곰 이미지 파일명을 적절히 변경하세요.
polar_bear_size = 50
polar_bear_x = width // 2 - polar_bear_size // 2
polar_bear_y = height - polar_bear_size - 20
polar_bear_speed = 5

# 얼음판 생성 함수
def create_ice_platform():
    size = random.randint(50, 150)
    x = random.randint(0, width - size)
    y = random.randint(0, height - size)
    return pygame.Rect(x, y, size, size)

# 초기 얼음판 생성
ice_platforms = [create_ice_platform() for _ in range(5)]

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    polar_bear_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * polar_bear_speed

    # 화면 밖으로 나가지 않도록 처리
    polar_bear_x = max(0, min(width - polar_bear_size, polar_bear_x))

    # 화면 업데이트
    screen.fill(white)
    screen.blit(background, (0, 0))

    # 북극곰 그리기
    screen.blit(pygame.transform.scale(polar_bear, (polar_bear_size, polar_bear_size)), (polar_bear_x, polar_bear_y))

    # 얼음판 그리기
    for platform in ice_platforms:
        pygame.draw.rect(screen, white, platform)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()