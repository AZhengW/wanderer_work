class Phone:
    def __init__(self, power, brand):
        self.power = power
        self.brand = brand

    def boot_up(self):
        if self.power <= 20:
            print("您的手机电量低,请及时充电")
        else:
            print("欢迎使用{}".format(self.brand))


iphone6s = Phone(20, "iPhone")
iphone6s.boot_up()
iphone11 = Phone(30, "iPhone")
iphone11.boot_up()
