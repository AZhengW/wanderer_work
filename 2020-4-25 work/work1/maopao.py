list = [10, 5, 2, 7,55,555,200]
for a in range(len(list)-1):
    for b in range(len(list) - 1 - a):
        if list[b] > list[b + 1]:
            list[b], list[b + 1] = list[b + 1], list[b]
print(list)

