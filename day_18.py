import random


# question 70
def question70():
    print(random.choice([x for x in range(0, 11) if x % 2 == 0]))
# question70()


# question 71
def question71():
    print(random.choice([x for x in range(10, 151) if x % 5 == 0 and x % 7 == 0]))
# question71()


# question 72
def question72():
    li = random.sample(range(100, 201), 5)
    print(li)
# question72()

# question 73
def question73():
    li = random.sample(range(100, 201, 2), 5)
    print(li)
# question73()


# question 74
def question74():
    li = random.sample([i for i in range(1, 1001) if i % 35 == 0], 5)
    print(li)
# question74()
