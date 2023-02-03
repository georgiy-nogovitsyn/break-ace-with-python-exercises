# question 60
def question60(n):
    if n == 0:
        return 0
    else:
        return question60(n-1) + 100
# n = int(input('Input: '))
# print(question60(n))


# question 61
def question61(num):
    if num < 2:
        return num
    else:
        return question61(num - 1) + question61(num - 2)
# num = int(input('Input: '))
# print(question61(num))


# question 62
def question62(num):
    arr = [0, 1]
    for x in range(num - 1):
        arr.append(arr[-2] + arr[-1])
    return arr
# num = int(input('Input: '))
# print( ','.join([str(x) for x in question62(num)]))


# question 63
def question63(num):
    for x in range(num+1):
        if x % 2 == 0:
            yield x
num = int(input('Input: '))
li = []
for i in question63(num):
    li.append(str(i))
print(','.join(li))


# question 64
def question64(num):
    for x in range(num+1):
        if x % 5 == 0 and x % 7 == 0:
            yield x
num = int(input('Input: '))
li = []
for i in question64(num):
    li.append(str(i))
print(','.join(li))
