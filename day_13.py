# question 47
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2 * 3.14


# question 48
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# question 49
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# question 50
def question50():
    raise(RuntimeError)
