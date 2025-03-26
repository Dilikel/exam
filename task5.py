def f (x):
    lists = [int(list) for list in str(x)]
    x1 = int(lists[0]) + int(lists[2]) +int(lists[4])
    x2 = int(lists[1]) + int(lists[3])
    return  int(str(x1) + str(x2))



