class Baby:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def breakfast(self):
        print("i m hungry")

    def sleep(self):
        print("我困了")


baby = Baby("张三", 20, "女")
print(baby.name, baby.age, baby.sex)
baby.breakfast()
baby.sleep()
