#  虚竹
#  只有血量,没有攻击力,每回合概率将人秒杀
import random


class Xuzhu:
    def __init__(self, hp, power):
        # 初始化定义虚竹的名字,武力值,血量
        self.hp = hp
        self.name = "虚竹"
        self.power = power

    def baoji(self):
        random1 = random.choice("bbbbbbbbbx")
        # 如果返回的的是x,就直接秒杀,虚竹无法暴击,因为返回值为a才能暴击,他没有
        return random1
