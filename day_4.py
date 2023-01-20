# question 14
def question14():
    line = input('Input: ')
    upper, lower = 0,0
    for x in line:
        if x.isalpha():
            if x.isupper():
                upper += 1
            else:
                lower += 1
    print(f'UPPER CASE {upper}\nLOWER CASE {lower}')
# question14()


# question 15
def question15():
    a = input('Input an integer: ')
    print(int(a) + int(a*2) + int(a*3) + int(a*4))
# question15()