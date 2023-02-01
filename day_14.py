# question 51
def question51():
    try:
        return 5/0
    except ZeroDivisionError:
        return 'Can\'t divison by zero'
# print(question51())


# question 52
class MyError(Exception):
    """Exception class

    Attributes:
        Err
    """
    def __init__(self, msg):
        self.msg = msg
# raise MyError('Wow')


# question 53
def question53():
    print('josh@google.com'.split('@')[0])
# question53()