# question 31
def question31():
    my_dict = {i:i**2 for i in range(1, 21)}
    print(my_dict)
# question31()


# question 32
def question32():
    my_dict = {i**2:i for i in range(1, 21)}
    print(my_dict.keys())
# question32()


# question 33
def question33():
    my_list = [i**2 for i in range(1, 21)]
    return my_list
# print(question33())


# question 34
def question34():
    print(question33()[0:6])
# question34()


# question 35
def question35():
    print(question33()[15:20])
# question35()


# question 36
def question36():
    print(question33()[5:])
# question36()


# question 37
def question37():
    print(tuple(question33()))
# question37()