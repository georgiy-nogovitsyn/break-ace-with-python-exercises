# question 90
def question90():
    dic = {}
    for x in 'abcdefgabc':
        if dic.get(x) == None:
            dic[x] = 1
        else:
            dic[x] = dic[x] + 1
    for item in dic.keys():
        print(f'{item},{dic[item]}')


# question 91
def question91():
    string = input('Input: ')
    print(string[::-1])
# question91()


# question 92
def question92():
    string = input('Input: ')
    print(string[::2])
# question92()


# question 93
def question93():
    import itertools
    print(list(itertools.permutations([1, 2, 3])))
# question93()


# question 94
def question94():
    for x in range(1, 36):
        if x * 2 + (35-x) * 4 == 94:
            print(f'chickens: {x}, rabbits: {35-x}')
            break
# question94()
