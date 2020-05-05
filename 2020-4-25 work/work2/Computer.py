class Computer:
    def __init__(self, type, price, brand):
        self.type = type
        self.price = price
        self.brand = brand

    def boot_up(self):
        print("欢迎使用价值{}{}牌{}".format(self.price, self.brand, self.type))


computer = Computer("笔记本",10000,"苹果")
computer.boot_up()
