# import library
import pygame
import BUTTONS

# pygame 초기화
pygame.init()

# 스크린
screen = pygame.display.set_mode((BUTTONS._SCREEN_WIDTH, BUTTONS._SCREEN_HEIGHT))
background = pygame.image.load("background/game_background_4.png")
background = pygame.transform.scale(background, (1280, 720))

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

# while loop 실행 조건
running = True
font = pygame.font.Font("Fonts/NanumMyeongjoExtraBold.ttf", 100)
title = font.render("Rain Stone", True, (0, 0, 0))

def startScreen():

    global running

    while running:
        clock.tick(60)
        screen.blit(background, (0, 0))
        screen.blit(title, (400, 100))

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "Quit"
            if event.type == pygame.MOUSEBUTTONUP:        # 마우스 클릭 이벤트
                curr_x, curr_y = event.pos
                if BUTTONS._START_BUTTON_RECT.collidepoint(curr_x, curr_y):        # 시작 화면의 Start Game을 누르면 스테이지 선택화면으로 넘어가도록 main에서 구현
                    print("Game Start")
                    return "Game Start"
                elif BUTTONS._EXIT_BUTTON_RECT.collidepoint(curr_x, curr_y):        # 시작 화면의 Quit을 누르면 게임이 종료되는 기능을 main에서 구현
                    running = False
                    return "Quit"

        # 시작 화면 버튼 올라가는 애니메이션
        if BUTTONS._START_BUTTON_RECT.y > BUTTONS._START_BUTTON_RECT_GOAL:
            BUTTONS._START_BUTTON_RECT.y -= 20
        elif BUTTONS._EXIT_BUTTON_RECT.y > BUTTONS._EXIT_BUTTON_RECT_GOAL:
            BUTTONS._EXIT_BUTTON_RECT.y -= 20


        # 작업한 스크린의 내용 저장
        screen.blits(blit_sequence=((BUTTONS._START_BUTTON, BUTTONS._START_BUTTON_RECT), (BUTTONS._EXIT_BUTTON, BUTTONS._EXIT_BUTTON_RECT)))

        # 작업한 스크린의 내용을 갱신하기
        pygame.display.flip()

'''if __name__ == '__main__':
    startScreen()'''
