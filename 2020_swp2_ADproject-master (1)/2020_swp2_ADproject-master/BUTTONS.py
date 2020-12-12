# import library
import pygame

# Define Buttons size
_SCREEN_WIDTH, _SCREEN_HEIGHT = 1280, 720
mainButtonSize = (400, 120)
stageButtonSize = (120, 120)


# main screen buttons
_START_BUTTON = pygame.image.load("icons/start_game.png")
_START_BUTTON = pygame.transform.scale(_START_BUTTON, mainButtonSize)
_START_BUTTON_RECT = _START_BUTTON.get_rect()
_START_BUTTON_RECT.centerx = round(_SCREEN_WIDTH / 2)
_START_BUTTON_RECT.centery = 780
_START_BUTTON_RECT_GOAL = 330

_EXIT_BUTTON = pygame.image.load("icons/exit.png")
_EXIT_BUTTON = pygame.transform.scale(_EXIT_BUTTON, mainButtonSize)
_EXIT_BUTTON_RECT = _EXIT_BUTTON.get_rect()
_EXIT_BUTTON_RECT.centerx = round((_SCREEN_WIDTH / 2))
_EXIT_BUTTON_RECT.centery = 950
_EXIT_BUTTON_RECT_GOAL = 500



# stage select screen buttons - stages
_STAGE_1 = pygame.image.load("icons/stage1.png")
_STAGE_1 = pygame.transform.scale(_STAGE_1, stageButtonSize)
_STAGE_1_SELECTED = pygame.image.load("icons/stage1_selected.png")
_STAGE_1_SELECTED = pygame.transform.scale(_STAGE_1_SELECTED, stageButtonSize)

_STAGE_2 = pygame.image.load("icons/stage2.png")
_STAGE_2 = pygame.transform.scale(_STAGE_2, stageButtonSize)
_STAGE_2_SELECTED = pygame.image.load("icons/stage2_selected.png")
_STAGE_2_SELECTED = pygame.transform.scale(_STAGE_2_SELECTED, stageButtonSize)

_STAGE_3 = pygame.image.load("icons/stage3.png")
_STAGE_3 = pygame.transform.scale(_STAGE_3, stageButtonSize)
_STAGE_3_SELECTED = pygame.image.load("icons/stage3_selected.png")
_STAGE_3_SELECTED = pygame.transform.scale(_STAGE_3_SELECTED, stageButtonSize)

_STAGE_4 = pygame.image.load("icons/stage4.png")
_STAGE_4 = pygame.transform.scale(_STAGE_4, stageButtonSize)
_STAGE_4_SELECTED = pygame.image.load("icons/stage4_selected.png")
_STAGE_4_SELECTED = pygame.transform.scale(_STAGE_4_SELECTED, stageButtonSize)

_STAGE_5 = pygame.image.load("icons/stage5.png")
_STAGE_5 = pygame.transform.scale(_STAGE_5, stageButtonSize)
_STAGE_5_SELECTED = pygame.image.load("icons/stage5_selected.png")
_STAGE_5_SELECTED = pygame.transform.scale(_STAGE_5_SELECTED, stageButtonSize)

_STAGE_6 = pygame.image.load("icons/stage6.png")
_STAGE_6 = pygame.transform.scale(_STAGE_6, stageButtonSize)
_STAGE_6_SELECTED = pygame.image.load("icons/stage6_selected.png")
_STAGE_6_SELECTED = pygame.transform.scale(_STAGE_6_SELECTED, stageButtonSize)

_STAGE_BUTTONS = [
    {'name': "STAGE1", 'button': _STAGE_1, 'selected': _STAGE_1_SELECTED, 'pos': (120, 100), 'locked': False, 'num':1},
    {'name': "STAGE2", 'button': _STAGE_2, 'selected': _STAGE_2_SELECTED, 'pos': (304, 100), 'locked': True, 'num':2},
    {'name': "STAGE3", 'button': _STAGE_3, 'selected': _STAGE_3_SELECTED, 'pos': (488, 100), 'locked': True, 'num':3},
    {'name': "STAGE4", 'button': _STAGE_4, 'selected': _STAGE_4_SELECTED, 'pos': (672, 100), 'locked': True, 'num':4},
    {'name': "STAGE5", 'button': _STAGE_5, 'selected': _STAGE_5_SELECTED, 'pos': (856, 100), 'locked': True, 'num':5},
    {'name': "STAGE6", 'button': _STAGE_6, 'selected': _STAGE_6_SELECTED, 'pos': (1040, 100), 'locked': True, 'num':6}
]

_LOCKED_IMAGE = pygame.image.load("icons/locked.png")
_LOCKED_IMAGE = pygame.transform.scale(_LOCKED_IMAGE, stageButtonSize)


# stage select screen buttons - others

_STAGE_START = pygame.image.load("icons/stage_start.png")
_STAGE_START = pygame.transform.scale(_STAGE_START, (200, 120))
_STAGE_START_RECT = _STAGE_START.get_rect()
_STAGE_START_RECT.x = 540
_STAGE_START_RECT.y = 580

_BACK = pygame.image.load("icons/back.png")
_BACK = pygame.transform.scale(_BACK, (120, 70))
_BACK_RECT = _BACK.get_rect()
_BACK_RECT.x, _BACK_RECT.y = 0, 0

_MISSION_TABLE = pygame.image.load("icons/mission_table.png")
_MISSION_TABLE = pygame.transform.scale(_MISSION_TABLE, (920, 290))

