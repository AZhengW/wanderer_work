class Bicycle:
    def __init__(self, power, age):
        self.age = age
        self.power = power

    def go(self):
        if self.age > 3:
            print("车辆过旧,请换电瓶")
        elif self.power < 10:
            print("电量低请及时充电")
        else:
            print("小鸟电动车欢迎您,注意带好头盔,安全驾驶")


bicycle = Bicycle(power=5, age=4)
bicycle.go()
