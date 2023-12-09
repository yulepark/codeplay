import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_size = 1024
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Image Display")

# 이미지 경로 설정
image_path = "ai_project/story_telling/image/01.png"  # 이미지 파일 경로로 변경해주세요
image_path = "ai_project/story_telling/image/02.png"
# 이미지 로드
try:
    image = pygame.image.load(image_path)
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# 이미지 크기 조정
image = pygame.transform.scale(image, (screen_size, screen_size))

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 이미지 표시
    screen.blit(image, (0, 0))

    # 화면 업데이트
    pygame.display.flip()

