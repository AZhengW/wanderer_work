#  虚竹
#  只有血量,没有攻击力,每回合概率将人秒杀
import random


class Xuzhu:
    def __init__(self, hp):
        self.hp = hp
        self.name = "虚竹"
        self.power = 100

    def kill_you(self):
        random1 = random.random()
        random2 = random.random()
        if random1 > random2:
            return 1
