import pygame
import random

farby_kociek = [(0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]
class kocka:
    x = 0
    y = 0
    druhy_kociek = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
    def __init_(self, x, y):
        self.x = x
        self.y = y
        self.typ = random.randint(0, len(self.druhy_kociek) -1)
        self.farba = random.randint(1, len(farby_kociek) -1)
        self.otacanie = 0
    def image(self):
        return self.druhy_kociek[self.typ][self.otacanie]


    def otacanie(self):
        self.otacanie = (self.otacanie + 1) % len(self.druhy_kociek[self.typ])
class Tetris:
    level = 2
    skore = 0
    zoom = 20
    state = "start"
    pole = []
    výška = 0
    šírka = 0
    x = 100
    y = 60
    kocka = None

    def __init__(self, výška,šírka):
        self.výška = výška
        self.šírka = šírka
        self.pole = []
        self.skore = 0
        self.state = "start"
        for i in range(výška):
            nová_rada = []
            for j in range(šírka):
                nová_rada.append(0)
            self.pole.append(nová_rada)
    def nova_kocka(self):
        self.kocka = kocka(3,0)
    def dotyk(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.kocka.image():
                    if i + self.kocka.y > self.vyska - 1 or \
                            j + self.kocka.x > self.sirka - 1 or \
                            j + self.kocka.x < 0 or \
                            self.pole[i + self.kocka.y][j + self.kocka.x] > 0:
                        intersection = True
        return intersection
    def zmiznutie_rady(self):
        rada = 0
        for i in range(1,self.vyska):
            nuly = 0
            for j in range(self.sirka):
                if self.pole[i][j] == 0:
                    nuly += 1
            if nuly == 0:
                rada += 1
                for i1 in range(i,1,-1):
                    for j in range(self.sirka):
                        self.pole[i][j] = self.pole[i1 - 1][j]
        self.score += rada ** 2










pygame.init()

čierna = (0,0,0)
biela = (255,255,255)
červená = (255,0,0)
zelená = (0,255,0)
žltá = (255,255,0)

veľkosť = 750,500
obrazovka = pygame.display.set_mode(veľkosť)
pygame.display.set_caption("Tetris")

done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris
počítadlo = 0

pressing_down = False

while not done:
    if game.kocka is None:
        game.nova_kocka()
    počítadlo += 1
    if počítadlo > 1000000:
        počítadlo = 0
    if počítadlo % (fps// game.level//2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()










pygame.quit()



