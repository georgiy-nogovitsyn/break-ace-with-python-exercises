# question 85
def question85():
    li = [item for i, item in enumerate([12, 24, 35, 70, 88, 120, 155]) if i not in [0, 4, 5]]
    print(li)
# question85()


# question 86
def question86():
    li = [12, 24, 35, 24, 88, 120, 155]
    li.remove(24)
    print(li)
# question86()


# question 87
def question87():
    li_one = [1, 3, 6, 78, 35, 55]
    li_two = [12, 24, 35, 24, 88, 120, 155]
    intersection = set(li_one) & set(li_two)
    print(intersection)
# question87()


# question 88
def question88():
    li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    for x in li:
        if li.count(x) > 1:
            li.remove(x)
    print(li)


# question 89
class Person:
    def __init__(self):
        self.gender = 'Unknown'

    def get_gender(self):
        print(self.gender)


class Male(Person):
    def __init__(self):
        self.gender = 'Male'


class Female(Person):
    def __init__(self):
        self.gender = 'Female'


marry = Female()
john = Male()
marry.get_gender()
john.get_gender()
