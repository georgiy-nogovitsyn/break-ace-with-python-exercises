# question 38
def question38():
    tp = tuple([i for i in range(11)])
    print(tp[:5])
    print(tp[5:])
# question38()


# question 39
def question39():
    tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    li = tuple([i for i in tp if i % 2 == 0])
    print(li)
# question39()


# question 40
def question40():
    inpt = input('Input: ')
    if inpt in ('Yes', 'YES', 'yes'): print('Yes')
    else: print('No')
# question40()


# question 41
def question41():
    li = list(map(lambda i: i**2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(li)
# question41()


# question 42
def question42():
    li = list(map(lambda i: i**2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print(li)
# question42()


# question 43
def question43():
    li = list(filter(lambda x: x % 2 == 0, range(1, 21)))
    print(li)
# question43()