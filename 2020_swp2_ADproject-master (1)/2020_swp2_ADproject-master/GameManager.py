import pygame
import BUTTONS

White = (255, 255, 255)
Black = (0, 0, 0)
class Player:
    def __init__(self):
        self.charactor = pygame.image.load('Sprite/shipGreen_manned.png')
        self.charactorSize = self.charactor.get_size()
        self.charactor = pygame.transform.scale(self.charactor, (int(self.charactorSize[0]/2.4), int(self.charactorSize[1]/2.4)))
        self.x_change = 2
        self.x = 371
        self.y = 600
        cx = 293
        self.charactorX = []
        for i in range(5):
            self.charactorX.append(cx)
            cx += 39

    def move(self, strMove):
        if (strMove == "-"):
            if self.x != self.charactorX[0]:
                    self.x_change -= 1
                    self.x = self.charactorX[self.x_change]
        elif(strMove == "+"):
            if self.x != self.charactorX[len(self.charactorX) - 1]:
                    self.x_change += 1
                    self.x = self.charactorX[self.x_change]


class GameManager:

    def __init__(self, stage):
        pygame.init()
        pygame.mixer.init()
        #sound
        self.shoot_effectSound = 'Assets/Resources/Sound/Effect/Hit.ogg'
        #UI
        self.font = pygame.font.Font("Fonts/NanumMyeongjoExtraBold.ttf", 30)
        self.combo = 0
        self.maxCombo = 0
        self.time = 0
        self.lowtime = pygame.time.get_ticks() / 1000
        self.dt = 0
        self.comboTime = 0
        self.comboStart = False;

        #result
        self.result_Background = pygame.image.load("Sprite/bg.png")
        self.result_Background = pygame.transform.scale(self.result_Background, (int(self.result_Background.get_size()[0] / 2), int(self.result_Background.get_size()[1] / 2)))

        self.result_winback = pygame.image.load("Sprite/win.png")
        self.result_loseback = pygame.image.load("Sprite/lose.png")
        self.result_winback = pygame.transform.scale(self.result_winback, (int(self.result_winback.get_size()[0] / 2), int(self.result_winback.get_size()[1] / 2)))
        self.result_loseback = pygame.transform.scale(self.result_loseback, (int(self.result_loseback.get_size()[0] / 2), int(self.result_loseback.get_size()[1] / 2)))

        self.result_table = pygame.image.load("Sprite/table.png")
        self.result_table = pygame.transform.scale(self.result_table, (int(self.result_table.get_size()[0] / 2), int(self.result_table.get_size()[1] / 2)))

        self.result_menubtn = pygame.image.load("Sprite/menu.png")
        self.result_retrybtn = pygame.image.load("Sprite/restart.png")
        self.result_nextbtn = pygame.image.load("Sprite/next.png")
        self.result_menubtn = pygame.transform.scale(self.result_menubtn, (int(self.result_menubtn.get_size()[0] / 2.4), int(self.result_menubtn.get_size()[1] / 2.4)))
        self.result_retrybtn = pygame.transform.scale(self.result_retrybtn, (int(self.result_retrybtn.get_size()[0] / 2.4), int(self.result_retrybtn.get_size()[1] / 2.4)))
        self.result_nextbtn = pygame.transform.scale(self.result_nextbtn, (int(self.result_nextbtn.get_size()[0] / 2.4), int(self.result_nextbtn.get_size()[1] / 2.4)))
        self.result_menubtn_rect = self.result_menubtn.get_rect(topleft = (480, 580))
        self.result_retrybtn_rect = self.result_retrybtn.get_rect(topleft = (580, 580))
        self.result_nextbtn_rect = self.result_nextbtn.get_rect(topleft = (680, 580))

        self.star_Background = [0 for i in range(3)]
        self.star = [0 for i in range(3)]
        self.starPos = [(470, 160), (560, 140), (665, 160)]
        self.starRot = [10, 0, -10]
        self.starSize = [2.8, 2.2, 2.8]

        self.goldMark = [0 for i in range(3)]
        self.xMark= [0 for i in range(3)]
        self.goldmarkPos = [(480, 300), (480, 400), (480, 500)]
        self.xmarkPos = [(485, 300), (485, 400), (485, 500)]

        for i in range(3):
            self.star_Background[i] = pygame.image.load("Sprite/star lock.png")
            self.star[i] = pygame.image.load("Sprite/star.png")
            self.star_Background[i] = pygame.transform.scale(self.star_Background[i], (int(self.star_Background[i].get_size()[0] / self.starSize[i]),
                                                                                       int(self.star_Background[i].get_size()[1] / self.starSize[i])))
            self.star[i] = pygame.transform.scale(self.star[i], (int(self.star[i].get_size()[0] / self.starSize[i]),
                                                                 int(self.star[i].get_size()[1] / self.starSize[i])))
            self.star_Background[i] = pygame.transform.rotate(self.star_Background[i], self.starRot[i])
            self.star[i] = pygame.transform.rotate(self.star[i], self.starRot[i])

            self.goldMark[i] = pygame.image.load("Sprite/gold medal.png")
            self.xMark[i] = pygame.image.load("Sprite/pointer location3.png")

            self.goldMark[i] = pygame.transform.scale(self.goldMark[i], (int(self.goldMark[i].get_size()[0] / 2.8),
                                                                 int(self.goldMark[i].get_size()[1] / 2.8)))
            self.xMark[i] = pygame.transform.scale(self.xMark[i], (int(self.xMark[i].get_size()[0] / 2.2),
                                                                 int(self.xMark[i].get_size()[1] / 2.2)))

        self.clear_misson = []

        #game
        self.isClear = False
        self.isEndgame = False
        x = 300
        y = 100
        self.pad_width = 1280
        self.pad_height = 720
        self.gamepad = pygame.display.set_mode((self.pad_width, self.pad_height))
        pygame.display.set_caption("stone")
        self.fps = pygame.time.Clock()

        self.background = pygame.image.load('Sprite/game_background_3. 2.png')
        self.backgroundSize = self.background.get_size()
        self.background = pygame.transform.scale(self.background, (int(self.backgroundSize[0] / 1.5), int(self.backgroundSize[1] / 1.5)))
        self.targetblock = pygame.image.load("Sprite/selectorA.png")
        self.targetblockSize = self.targetblock.get_size()
        self.targetblock = pygame.transform.scale(self.targetblock, (int(self.targetblockSize[0] * 1.8), int(self.targetblockSize[1] * 1.8)))
        self.backblock = pygame.image.load("Sprite/selectorB.png")

        self.targetblockX = 100
        self.targetblockY = [250, 350, 450]

        bColor = ['red', 'yellow', 'blue', 'green', 'purple', 'gray']
        self.blocks = [0 for i in range(len(bColor))]
        for i in range(len(bColor)):
            self.blocks[i] = pygame.image.load("Sprite/" + bColor[i] + "_Block.png")
            self.blockSize = self.blocks[i].get_size()
            self.blocks[i] = pygame.transform.scale(self.blocks[i], (int(self.blockSize[0] * 1.22), int(self.blockSize[1] * 1.22)))

        self.resultblock = []
        self.backblockX = []
        self.backblockY = []
        self.checkblock = []
        self.stageblocks = [[0 for i in range(5)] for j in range(14)]
        for i in range(5):
            self.backblockX.append(x)
            x += 39
        for i in range(14):
            self.backblockY.append(y)
            y += 39

        self.playerLaser = pygame.image.load("Sprite/simple_patten.png")
        self.playerLaserSize = self.playerLaser.get_size()
        self.playerLaser = pygame.transform.scale(self.playerLaser, (int(self.playerLaserSize[0] * 2), int(self.playerLaserSize[1] / 9)))
        self.playerLaser = pygame.transform.rotate(self.playerLaser, 270)
        self.playerLaser.set_alpha(200)

        self.colorPanel = pygame.image.load("Sprite/Square.jpg")
        self.colorPanel = pygame.transform.scale(self.colorPanel, (int(self.colorPanel.get_size()[0]/2.6), int(self.colorPanel.get_size()[1] * 1.09)))
        self.colorPanel.set_alpha(100)
        self.colorPanel_colors = [(255, 0, 0), (255, 255, 0), (0, 0, 255), (0, 255, 0), (138, 43, 226), (128, 128, 128)]

        #readtxt
        for i in range(14):
            for j in range(5):
                self.stageblocks[i][j] = self.readtxt(stage)[i][j]

        for i in range(14, 16):
            self.clear_misson.append(self.readtxt(stage)[i].strip())

        self.clearStr = ["게임 클리어", "콤보 {}".format(self.clear_misson[0]) + "이상", self.clear_misson[1] + "초 이내 클리어"]

        self.clearLabel = [0 for i in range(3)]
        self.clearLabelPos = [(580, 315), (580, 415), (580, 515)]
        for i in range(3):
            self.clearLabel[i] = self.font.render(self.clearStr[i], True, Black)

    def game(self, stage):
        player = Player()

        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if (not self.isEndgame):
                    if event.type == pygame.QUIT:
                        crashed = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.move("-")
                        elif event.key == pygame.K_RIGHT:
                            player.move("+")
                        if event.key == pygame.K_SPACE:
                            self.check_blocks(player)
                else:
                    if event.type == pygame.MOUSEBUTTONUP:
                        curr_x, curr_y = event.pos
                        if self.result_menubtn_rect.collidepoint(curr_x, curr_y):
                            print(1)
                            return "Select_Stage"
                        elif self.result_retrybtn_rect.collidepoint(curr_x, curr_y):
                            print(2)
                            return "Retry"
                        elif self.result_nextbtn_rect.collidepoint(curr_x, curr_y):
                            print(3)
                            return "Next_Stage"

            self.render(player, stage)

            pygame.display.update()
            self.fps.tick(60)
            pygame.display.flip()

    def render(self, player, stage):
        # rendering
        self.gamepad.fill(White)
        self.gamepad.blit(self.background, (0, 0))
        self.gamepad.blit(self.colorPanel, (300, 100))
        for i in range(3):
            self.gamepad.blit(self.targetblock, (self.targetblockX, self.targetblockY[i]))
        for i in range(0, 14):
            for j in range(0, 5):
                self.gamepad.blit(self.backblock, (self.backblockX[j], self.backblockY[i]))

        self.gamepad.blit(self.playerLaser, (player.x + 19, 100))
        for i in range(0, 14):
            for j in range(0, 5):
                if self.stageblocks[i][j] != '0':
                    self.gamepad.blit(self.blocks[int(self.stageblocks[i][j]) - 1],
                                      (self.backblockX[j] + 0.5, self.backblockY[i] + 0.5))

        for i in range(len(self.resultblock)):
            self.gamepad.blit(self.blocks[self.resultblock[i]], (self.targetblockX + 15, self.targetblockY[i] + 13))

        self.comboUI = self.font.render("Combo : " + str(self.combo), True, White)
        self.timeUI = self.font.render("Time : " + str(self.time), True, White)
        self.gamepad.blit(self.comboUI, (800, 200))
        self.gamepad.blit(self.timeUI, (800, 350))
        self.gamepad.blit(player.charactor, (player.x, player.y))

        if not self.isEndgame:
            self.time = int(pygame.time.get_ticks() / 1000 - self.lowtime)
            if len(self.resultblock) == 3:
                if len(set(self.checkblock)) == 1:
                    self.resultblock = []
                    self.checkblock = []
                    self.combo += 1
                    self.comboTime = 0
                    self.dt = pygame.time.get_ticks() / 1000
                    self.comboStart = True
                    if self.maxCombo < self.combo:
                        self.maxCombo = self.combo
                else:
                    self.isEndgame = True

            if self.comboStart:
                self.comboTime = pygame.time.get_ticks() / 1000 - self.dt
                if self.comboTime >= 2.5:
                    self.combo = 0
                    self.comboStart = False

            self.zerocurrent = sum([len(set(self.stageblocks[i])) for i in range(len(self.stageblocks))])

            if self.zerocurrent == 14:
                if len(BUTTONS._STAGE_BUTTONS) > stage:
                    BUTTONS._STAGE_BUTTONS[stage]['locked'] = False
                self.isClear = True
                self.isEndgame = True
        else:
            self.gamepad.blit(self.result_Background, (400, 40))
            self.gamepad.blit(self.result_table, (430, 180))
            self.gamepad.blit(self.result_menubtn, (480, 580))
            self.gamepad.blit(self.result_retrybtn, (580, 580))

            if self.isClear:
                self.gamepad.blit(self.result_winback, (380, 30))
                self.gamepad.blit(self.result_nextbtn, (680, 580))
                for i in range(3):
                    self.gamepad.blit(self.clearLabel[i], self.clearLabelPos[i])
                    self.gamepad.blit(self.star_Background[i], self.starPos[i])
                self.gamepad.blit(self.star[0], self.starPos[0])
                self.gamepad.blit(self.goldMark[0], self.goldmarkPos[0])

                if self.maxCombo >= int(self.clear_misson[0]) or self.time < int(self.clear_misson[1]):
                    self.gamepad.blit(self.star[2], self.starPos[2])
                if self.maxCombo >= int(self.clear_misson[0]) and self.time < int(self.clear_misson[1]):
                    self.gamepad.blit(self.star[1], self.starPos[1])
                    self.gamepad.blit(self.star[2], self.starPos[2])

                if self.maxCombo >= int(self.clear_misson[0]):
                    self.gamepad.blit(self.goldMark[1], self.goldmarkPos[1])
                else:
                    self.gamepad.blit(self.xMark[1], self.xmarkPos[1])

                if self.time < int(self.clear_misson[1]):
                    self.gamepad.blit(self.goldMark[2], self.goldmarkPos[2])
                else:
                    self.gamepad.blit(self.xMark[2], self.xmarkPos[2])
            else:
                self.gamepad.blit(self.result_loseback, (380, 30))
                for i in range(3):
                    self.gamepad.blit(self.xMark[i], self.xmarkPos[i])
                    self.gamepad.blit(self.clearLabel[i], self.clearLabelPos[i])
                    self.gamepad.blit(self.star_Background[i], self.starPos[i])

    def check_blocks(self, player):
        for i in range(13, -1, -1):
            if self.stageblocks[i][player.x_change] != '0':
                pygame.mixer.music.load(self.shoot_effectSound)
                pygame.mixer.music.play(0)
                self.resultblock.append(int(self.stageblocks[i][player.x_change]) - 1)
                self.checkblock.append(self.stageblocks[i][player.x_change])
                self.colorPanel.fill(
                    self.colorPanel_colors[int(self.stageblocks[i][player.x_change]) - 1])
                self.playerLaser.fill(
                    self.colorPanel_colors[int(self.stageblocks[i][player.x_change]) - 1])
                self.stageblocks[i][player.x_change] = '0'
                break

    def readtxt(self, stage):
        f = open("Assets/Resources/Stage/stage{}".format(stage) + ".txt", "r")
        line = f.readlines()
        f.close()
        return line