#question 20
class DivisibleBy7:
    def func():
        num = int(input('Input: '))
        for x in range(num+1):
            if x % 7 == 0:
                print(x)
#DivisibleBy7.func()