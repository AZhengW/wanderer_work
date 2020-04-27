#统一概率方法
import random
def probability():
    random1=random.randint(1,100)
    random2=random.randint(1,100)
    if random1*2>random2%2:
        return 1
    else:
        return 0

