list = [10, 5, 2, 7, 55, 555, 200]
for a in range(len(list) - 1):  # 定义循环次数
    for b in range(len(list) - 1 - a):  # 定义对比次数,每次减少一次,因为每一次的最大值都在最后面,所以不用比较
        if list[b] > list[b + 1]:
            list[b], list[b + 1] = list[b + 1], list[b]
print(list)
