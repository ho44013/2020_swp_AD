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
_START_BUTTON_RECT.centery = 710
_START_BUTTON_RECT_GOAL = 260

_OPTION_BUTTON = pygame.image.load("icons/option.png")
_OPTION_BUTTON = pygame.transform.scale(_OPTION_BUTTON, mainButtonSize)
_OPTION_BUTTON_RECT = _OPTION_BUTTON.get_rect()
_OPTION_BUTTON_RECT.centerx = round(_SCREEN_WIDTH / 2)
_OPTION_BUTTON_RECT.centery = 850
_OPTION_BUTTON_RECT_GOAL = 400

_EXIT_BUTTON = pygame.image.load("icons/exit.png")
_EXIT_BUTTON = pygame.transform.scale(_EXIT_BUTTON, mainButtonSize)
_EXIT_BUTTON_RECT = _EXIT_BUTTON.get_rect()
_EXIT_BUTTON_RECT.centerx = round((_SCREEN_WIDTH / 2))
_EXIT_BUTTON_RECT.centery = 990
_EXIT_BUTTON_RECT_GOAL = 540



# stage select screen buttons - stages
_STAGE_1 = pygame.image.load("icons/stage1.png")
_STAGE_1 = pygame.transform.scale(_STAGE_1, stageButtonSize)

_STAGE_2 = pygame.image.load("icons/stage2.png")
_STAGE_2 = pygame.transform.scale(_STAGE_2, stageButtonSize)

_STAGE_3 = pygame.image.load("icons/stage3.png")
_STAGE_3 = pygame.transform.scale(_STAGE_3, stageButtonSize)

_STAGE_4 = pygame.image.load("icons/stage4.png")
_STAGE_4 = pygame.transform.scale(_STAGE_4, stageButtonSize)

_STAGE_5 = pygame.image.load("icons/stage5.png")
_STAGE_5 = pygame.transform.scale(_STAGE_5, stageButtonSize)

_STAGE_BUTTONS = [
    {'name': "STAGE1", 'button': _STAGE_1, 'pos': (140, 100), 'locked': False, 'num':1},
    {'name': "STAGE2", 'button': _STAGE_2, 'pos': (360, 100), 'locked': True, 'num':2},
    {'name': "STAGE3", 'button': _STAGE_3, 'pos': (580, 100), 'locked': True, 'num':3},
    {'name': "STAGE4", 'button': _STAGE_4, 'pos': (800, 100), 'locked': True, 'num':4},
    {'name': "STAGE5", 'button': _STAGE_5, 'pos': (1020, 100), 'locked': True, 'num':5}
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

