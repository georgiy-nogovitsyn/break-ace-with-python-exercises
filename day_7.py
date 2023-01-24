# question 20
class DivisibleBy7:
    def func():
        num = int(input('Input: '))
        for x in range(num+1):
            if x % 7 == 0:
                print(x)
#DivisibleBy7.func()


# question 21
def question21():
    from math import sqrt
    position = 0, 0
    while True:
        step = input('Input: ').split()
        if not step:
            break
        elif step[0] == 'UP':
            position = position[0] + int(step[-1]), position[1]
        elif step[0] == 'DOWN':
            position = position[0] - int(step[-1]), position[1]
        elif step[0] == 'RIGHT':
            position = position[0], position[1] + int(step[-1])
        elif step[0] == 'LEFT':
            position = position[0], position[1] - int(step[-1])
    print(round(sqrt((position[0]**2 + position[1]**2))))
#question21()



