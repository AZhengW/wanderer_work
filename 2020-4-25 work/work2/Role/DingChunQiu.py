#  丁春秋类:
#  初始hp10000,攻击力500,每回合有百分之10的几率回血500
class DingChunQiu:
    def __init__(self,hp,power):
        self.name="丁春秋"
        self.hp=hp
        self.power=power
    def add_blood(self):
        self.hp= self.hp + 500
        print("看我回血")