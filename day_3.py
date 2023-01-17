# question 10
def question10():
    lst = sorted(list(set((input('Input sequence here: ').split(' ')))))
    print(' '.join(lst))
# question10()


# question 11
def question11():
    lst = list(input('Input sequence here: ').split(','))
    lst1 = []
    for x in lst:
        if int(x, base=2) % 5 == 0:
            lst1.append(x)
    print(','.join(lst1))
# question11()


# question 12
def question12():
    lst = []
    for x in range(1000, 3001):
        for it, y in enumerate(str(x)):
            if int(y) % 2 != 0:
                break
            elif it + 1 == len(str(x)):
                lst.append(str(x))

    print(','.join(lst))
# question12()


# question 13
def question13():
    line = input('Input: ')
    letters = 0
    digit = 0
    for ch in line:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digit += 1
    print(f'LETTERS {letters}\nDIGITS {digit}')
#question13()