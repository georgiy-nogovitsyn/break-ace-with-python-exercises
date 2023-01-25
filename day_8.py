# question 22
def question22():
    string = sorted(input('Input: ').split(' '))
    dic = {i:string.count(i) for i in string}
    for x in dic:
        print(f'{x}:{dic.get(x)}')
#question22()


# question 23
def question23(a):
    return a ** 2
#print(question23(int(input(': '))))

# question 24
print(f'{abs.__doc__}\n\n\n{int.__doc__}\n\n\n{input.__doc__}')

def question24(a):
    '''
    Draw a square by side size 'a'.
    :param a must be an integer:
    '''
    for x in range(a):
        print(' * ' * a)
#question24(10)
