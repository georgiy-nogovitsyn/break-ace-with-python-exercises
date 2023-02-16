# question 95
def question95():
    scores = input('Input: ')
    list_of_scores = scores.split(' ')
    list_of_scores = [int(x) for x in list_of_scores]
    print(sorted(set(list_of_scores))[-2])
# question95()


# question 96
def question96():
    import textwrap
    s = input('Input a string: ')
    width = int(input('Input a width: '))
    print(textwrap.fill(s,width))
# question96()


# question 97
def question97():
    pass


# question 98
def question98():
    import calendar
    s = input('Input: ').split(' ')
    date = []
    for x in s:
        if x[0] == 0:
            date.append(int(x[-1]))
        else:
            date.append(int(x))
    print(calendar.day_name[calendar.weekday(date[-1], date[0], date[1])].upper())
# question98()


# question 99
def question99():
    pass
