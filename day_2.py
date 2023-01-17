from math import sqrt


# question 4
def question4():
    list_of_num = input('Input comma-separated numbers: ').split(',')
    print(list_of_num)
    print(tuple(list_of_num))
# question4()


# question 5
class String():
    def get_string(self):
        self.string = input('Input string: ')

    def print_string(self):
        print(self.string.upper())


def test_func():
    test = String()
    test.get_string()
    test.print_string()
# test_func()


# question 6
def question6():
    lst = input('Enter a comma-separated sequance: ').split(',')
    lst1 = []
    for d in lst:
        lst1.append(str(round(sqrt((2 * 50 * int(d)) / 30))))
    print(','.join(lst1))
# question6()


# question 7
def question7():
    x_y = input('Input X and Y: ')
    matrix = [[x * y for y in range(int(x_y[-1]))] for x in range(int(x_y[0]))]
    print(matrix)
# question7()


# question 8
def question8():
    lst = sorted(list(input('Input: ').split(',')))
    print(','.join(lst))
# question8()


# question 9
def question9():
    lst = []
    while True:
        line = input('Input your line here: ')
        if len(line) == 0:
            break
        lst.append(line.upper())
    for line in lst:
        print(line)
# question9()