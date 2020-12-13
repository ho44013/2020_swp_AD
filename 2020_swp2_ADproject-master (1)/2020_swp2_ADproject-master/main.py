# Import Library
import pygame
import startscreen
from selectStages import Stage
import selectStages
import BUTTONS
from GameManager import GameManager

# Initialize the game
pygame.init()
pygame.display.set_caption("Stone")

# 스크린 크기 및 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = True
_MAIN_SCREEN = True
_STAGE_SELECT = False
_GAME_SCENE = False

selectStage = Stage()

while running:

    if _MAIN_SCREEN:
        startConse = startscreen.startScreen()
        if startConse == "Quit":    # 시작화면에서 Quit 누른 경우 프로그램 종료
            running = False
        elif startConse == "Game Start":    # 시작화면에서 Game Start 누른 경우 시작화면 끄고 스테이지 선택 화면
            _MAIN_SCREEN = False
            selectStages._UNLOCKED_STAGE_SELECT = False
            _STAGE_SELECT = True
    elif _STAGE_SELECT:
        stageConse = selectStage.selectStage()
        if stageConse == "Quit":    # 스테이지 선택화면에서 Quit 누른 경우 프로그램 종료
            running = False
        elif stageConse == "Back to Start":    # 스테이지 선택화면에서 Back 누른 경우 스테이지 선택화면 끄고 시작 화면
            _MAIN_SCREEN = True
            _STAGE_SELECT = False
        elif stageConse == "StartGame":
            _STAGE_SELECT = False
            _GAME_SCENE = True
    elif _GAME_SCENE:
        stageConse = GameManager(selectStage.stage_info)
        games = stageConse.game(selectStage.stage_info)
        if games == "Quit":
            running = False
        elif games == "Select_Stage":
            _GAME_SCENE = False
            selectStages._UNLOCKED_STAGE_SELECT = False
            _STAGE_SELECT = True
        elif games == "Retry":
            print("retry")
        elif games == "Next_Stage":
            selectStage.stage_info += 1

















