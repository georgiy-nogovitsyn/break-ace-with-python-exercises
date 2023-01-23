# question 18
def question18():
    import re
    lst = input('Input: ').split(',')
    new_lst = []
    pattern = re.compile(r'^.(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@"]).*$')
    for x in lst:
        if pattern.match(x) is not None and 6 < len(x) <= 12:
            new_lst.append(x)
    print(','.join(new_lst))
# question18()


def question19():
    lst = []
    while True:
        x = input().split(',')
        if not x[0]:
            break
        lst.append(tuple(x))
    lst.sort()
    print(lst)
# question19()
