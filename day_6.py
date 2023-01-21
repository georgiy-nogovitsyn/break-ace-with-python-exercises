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
#question18()

def question19():
    lst = []
    new_lst = []
    while True:
        x = input().split()
        if x:
            lst.append(x)
        elif not x:
            break
        for y in lst:
            wrap = []
            for z in y:
                wrap.append(z)
            new_lst.append(tuple(z))
    print(new_lst)
question19()
