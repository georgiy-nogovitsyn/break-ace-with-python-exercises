# question 65
import random


def question65():
    li = [2, 4, 6, 8]
    for x in li:
        assert x % 2 == 0
# question65()


# question 66
def question66():
    print(eval(input('Input: ')))
# question66()


# question 67
def binary_search(arr, num):
    first = 0
    last = len(arr) - 1
    while first <= last:
        middle = first + (last - first) // 2
        if arr[middle] == num:
            return middle
        elif arr[middle] < num:
            first = middle + 1
        else:
            last = middle - 1
    return -1

arr = [9, 2, 3, 4, 5, 8, 0, 1]
print(binary_search(sorted(arr), 2))


# question 68
def question68():
    print(random.random() * 100)
# question68()


# question 69
def question69():
    print(random.uniform(5, 95))
# question69()