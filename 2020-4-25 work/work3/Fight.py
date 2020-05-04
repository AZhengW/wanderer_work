# 对打规则: 一对一,直到一方死亡为止
# 概率暴击,童姥暴击率>春秋,虚竹有概率秒杀,童姥血量小于2000大于0的时候会触发自身的技能
from Role import XuZhu, DingChunQiu, TongLao


class Fight:
    def __init__(self, role1, role2):
        self.role1 = role1
        self.role2 = role2

    def fight(self):
        while True:
            if self.role2.baoji() == "x":  # 首先判断角色中的暴击方法是否返回x,如果返回x,就代表触发了秒杀
                self.role2.power = self.role2.power * 100000  # 触发秒杀的角色武力值提升10000000倍
                print("对不起你死了,虚竹我发狂了!")  # 这是嘲讽的语句233~
            elif self.role2.baoji() == "a":  # 如果没有随机到x就判断是否随机到a,如果随机到a,武力值翻倍
                self.role2.power = self.role2.power * 2
                print(self.role2.name + "的武力值提升了两倍!!  的")
            self.role1.hp = self.role1.hp - self.role2.power  # 血量计算
            print("{}受到了{}{}伤害,还剩{}血".format(self.role1.name, self.role2.name, self.role2.power,
                                             self.role1.hp))  # 打印血量计算结果
            if 3000 > self.role1.hp > 0 and self.role1.name == "童姥":  #判断血量是否到3000一下,且角色为童姥,如果是的话就调用童姥的暴怒技能
                print(self.role1.bao_nu())
            if self.role1.hp <= 0 or self.role2.hp <= 0:  # 判断是否一方HP=
                print(self.role1.name + "死了,", self.role2.name + "赢了.")  # 如果一方hp=0,那么把谁输谁赢打印出来 ,且结束循环
                break

                # 下面代码跟上面同理,上面是角色1被角色二打了,下面是角色二被角色一打.过程相同
            if self.role1.baoji() == "x":
                self.role1.power = self.role1.power * 100000
                print("对不起你死了,虚竹我发狂了!")
            if self.role1.baoji() == "a":
                self.role1.power = self.role1.power * 2
                print(self.role1.name + "的武力值提升了两倍!!")
            self.role2.hp = self.role2.hp - self.role1.power
            print("{}受到了{}{}伤害,还剩{}血".format(self.role2.name, self.role1.name, self.role1.power, self.role2.hp))
            if 3000 > self.role2.hp > 0 and self.role2.name == "童姥":
                self.role2.bao_nu()
            if self.role1.hp <= 0 or self.role2.hp <= 0:
                print(self.role2.name + "死了,", self.role1.name + "赢了.")
                break
            else:
                continue


xuzhu = XuZhu.Xuzhu(5000, 2000)
tonglao = TongLao.Tonglao(20000, 500)
dingchunqiu = DingChunQiu.DingChunQiu(10000,500)
go = Fight(xuzhu, dingchunqiu)
go.fight()
