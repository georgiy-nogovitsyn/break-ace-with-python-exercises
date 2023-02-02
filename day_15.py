# question 54
def question54():
    import re
    email = input('Input: ')
    exp_re = '(\w+)@(\w+).(com)'
    co = re.match(exp_re, email)
    print(co.group(2))
# question54()


# question 55
def question55():
    string = input('Input: ')
    li = []
    for x in string:
        if x.isdigit():
            li.append(x)
    print(li)
# question55()


# question 56
def question56():
    string = u'hello world!'
    print(string)
# question56()


# question 57
def question57():
    s = input('Input: ')
    u = s.encode('utf-8')
    print(u)
# question57()


# question 58
# -*- coding: utf-8 -*-


# question 59
def question59():
    n = int(input('Input: '))
    total = 0
    for x in range(1, n+1):
        total += x/(x+1)
    print(round(total, 2))
# question59()


