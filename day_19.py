import random
# question 75
def question75():
    print(random.randrange(7, 16))


# question 76
def question76():
    import zlib
    s = 'hello world!hello world!hello world!hello world!'
    s = bytes(s, 'utf-8')
    s = zlib.compress(s)
    print(s)
    print(zlib.decompress(s))
# question76()


# question 77
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper
@performance
def question77():
    for x in range(100):
        1 + 1
# question77()


# question 78
def question78():
    li = [3, 6, 7, 8]
    random.shuffle(li)
    print(li)
# question78()


# question 79
def question79():
    li = [['I', 'You'], ['Play', 'Love'], ['Hockey', 'Football']]
    for x in li[0]:
        for y in li[1]:
            for z in li[2]:
                print(f'{x} {y} {z}')
# question79()

