# 对打规则: 一对一,直到一方死亡为止,死亡了就调用seepeople方法
# 概率暴击,概率闪避,童姥暴击率>春秋,闪避概率随机,血量小的先手(暂不考虑血量相等情况)
from Role import XuZhu, DingChunQiu, TongLao
import probability


class Fight:
    def __init__(self, role1, role2):
        self.role1 = role1
        self.role2 = role2

    def fight(self):
        while True:
            if probability.probability() == 1:
                self.role2.power=self.role2.power*2
                print(self.role2.name+"暴击了!")
            self.role1.hp = self.role1.hp - self.role2.power
            print("{}受到了{}{}伤害,还剩{}血".format(self.role1.name, self.role2.name, self.role2.power, self.role1.hp))
            if self.role1.hp <= 0 or self.role2.hp <= 0:
                print(self.role1.name + "输了,", self.role2.name + "赢了.")
                break
            if probability.probability() == 0:
                self.role1.power = self.role1.power * 2
                print(self.role1.name + "暴击了!")
            self.role2.hp = self.role2.hp - self.role1.power
            print("{}受到了{}{}伤害,还剩{}血".format(self.role2.name, self.role1.name, self.role1.power, self.role2.hp))
            if self.role1.hp <= 0 or self.role2.hp <= 0:
                print(self.role2.name + "输了,", self.role1.name + "赢了.")
                break
            else:
                continue


xuzhu = XuZhu.Xuzhu(5000)
tonglao = TongLao.Tonglao(5000, 50)
gan = Fight(xuzhu, tonglao)
gan.fight()
