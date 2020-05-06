class people:

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old" % (self.name, self.age))


p = people('tom', 10, 30)
p.speak()
