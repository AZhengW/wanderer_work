list1 = [-4, -1, 0, 3, 10]
list2 = [-7, -3, 2, 3, 11]


def dosort(list3):
    new_list = ([i ** 2 for i in list3])  # 遍历列表数据,每一个数据都平方
    new_list.sort()  # 对列表排序
    print(new_list)


dosort(list1)
dosort(list2)
