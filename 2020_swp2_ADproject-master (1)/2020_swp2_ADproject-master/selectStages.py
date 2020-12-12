# import Library
import pygame
import BUTTONS

# pygame 초기화
pygame.init()

# 스크린
screen = pygame.display.set_mode((BUTTONS._SCREEN_WIDTH, BUTTONS._SCREEN_HEIGHT))
background = pygame.image.load("background/game_background_4.png")
background = pygame.transform.scale(background, (1280, 720))

# 프레임 설정을 위한 Clock 생성
clock = pygame.time.Clock()


running = True   # while loop 실행의 조건
_UNLOCKED_STAGE_SELECT = False    # 해금된 스테이지의 선택 유무 - False면 _STAGE_START가 보이지 않음
class Stage():
    def __init__(self):
        self.stage_info = 0
        self.font = pygame.font.Font("Fonts/NanumMyeongjoExtraBold.ttf", 30)

    def readtxt(self, stage):
        f = open("Assets/Resources/Stage/stage{}".format(stage) + ".txt", "r")
        line = f.readlines()
        f.close()
        return line

    def selectStage(self):

        global running, _UNLOCKED_STAGE_SELECT
        self.stage_info = 0

        while running:
            clock.tick(30)
            screen.blit(background, (0,0))


            # 이벤트 처리
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return "Quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:        # 스테이지 언락키, 이스터에그로 남겨두거나 추후 삭제 가능
                        for b in BUTTONS._STAGE_BUTTONS:
                            if b['locked']:
                                b['locked'] = False
                                print(b['name'],"unlocked")
                                break
                            else:
                                continue
                if event.type == pygame.MOUSEBUTTONUP:    # 마우스 클릭
                    curr_x, curr_y = event.pos
                    if BUTTONS._BACK_RECT.collidepoint(curr_x, curr_y):    # _BACK 누르면 start 화면으로 돌아가는 기능을 main에 추가
                        return "Back to Start"
                    for b in BUTTONS._STAGE_BUTTONS:
                        if (not b['locked']) and b['button'].get_rect(topleft = b['pos']).collidepoint(curr_x, curr_y):    # 해금되어있는 스테이지를 클릭하면 _STAGE_START가 보이게
                            _UNLOCKED_STAGE_SELECT = True
                            self.stage_info = b['num']
                    if (_UNLOCKED_STAGE_SELECT) and BUTTONS._STAGE_START_RECT.collidepoint(curr_x, curr_y):        # _STAGE_START를 누르면 게임이 시작되게 - return으로 main에 전달 예정
                        print("start")
                        return "StartGame"

            for b in BUTTONS._STAGE_BUTTONS:    # stage들 추가 (해금이 안 된 상태면 자물쇠, 해금된 상태면 스테이지)
                if b['locked']:
                    screen.blit(BUTTONS._LOCKED_IMAGE, b['pos'])
                else:
                    if b['num'] == self.stage_info:
                        screen.blit(b['selected'], b['pos'])
                    else:
                        screen.blit(b['button'], b['pos'])


            screen.blit(BUTTONS._BACK, BUTTONS._BACK_RECT)  # Back 버튼

            self.clear_misson = []
            self.clearLabel = [i for i in range(3)]
            self.clearLabelPos = [(230, 300), (230, 400), (230, 500)]



            if _UNLOCKED_STAGE_SELECT:        # 현재 해금된 스테이지를 클릭했는지
                screen.blit(BUTTONS._STAGE_START, (540, 580))

                screen.blit(BUTTONS._MISSION_TABLE, (180, 270))

                for i in range(14, 16):
                    self.clear_misson.append(self.readtxt(self.stage_info)[i].strip())
                self.clearStr = ["-  게임 클리어", "-  콤보 {}".format(self.clear_misson[0]) + "이상",
                                 "-  " + self.clear_misson[1] + "초 이내 클리어"]
                for i in range(3):
                    self.clearLabel[i] = self.font.render(self.clearStr[i], True, (0, 0, 0))
                for i in range(3):
                    screen.blit(self.clearLabel[i], self.clearLabelPos[i])


            # 화면에 업데이트
            pygame.display.update()



'''if __name__ == '__main__':
    selectStage()'''
