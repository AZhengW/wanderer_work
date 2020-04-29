#  天山童姥类:
#  初始hp10000,攻击力800,当血量<5000时,攻击力翻三倍,血量扣除一半,只生效一次
import random


class Tonglao():
    def __init__(self, hp, power):
        self.name = "童姥"
        self.hp = hp
        self.power = power

    def bao_nu(self):
        self.hp = self.hp / 2
        self.power = self.power * 3
        print("童姥说:小鬼,你惹怒我了!!,自身血量减半,武力值*3")

    def baoji(self):
        random1 = random.choice("aaaabbbbb")
        return random1
