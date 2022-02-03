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


    def rotate(self):
        self.otacanie = (self.otacanie + 1) % len(self.druhy_kociek[self.typ])
class Tetris:
    level = 2
    score = 0
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
    self.pole = 0
    self.score = 0
    self.state = "start"
    for i in range(výška):
        nová_rada = []
        for j in range(šírka):
            nová_rada.append(0)
        self.pole.append(nová_rada)

