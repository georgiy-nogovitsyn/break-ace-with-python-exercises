# question 80
def question80():
    li = [i for i in [5, 6, 77, 45, 22, 12, 24] if i % 2 != 0]
    print(li)
# question80()


# question 81
def question81():
    li = [i for i in [12, 24, 35, 70, 88, 120, 155] if i % 35 != 0]
    print(li)
# question81()


# question 82
def question82():
    li = [item for i, item in enumerate([12, 24, 35, 70, 88, 120, 155]) if i % 2 != 0 and i <=6]
    print(li)
# question82()


# question 83
def question83():
    li = [item for i, item in enumerate([12, 24, 35, 70, 88, 120, 155]) if i not in range(2,5)]
    print(li)
# question83()


# question 84
def question84():
    li = [[[0 for x in range(8)] for x in range(5)] for x in range(3)]
    print(li)
# question84()
