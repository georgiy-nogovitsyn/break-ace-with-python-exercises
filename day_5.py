# question 16
def question16():
    new_lst = [str(int(x) ** 2) for x in input('Input: ').split(',') if int(x) % 2 != 0]
    print(','.join(new_lst))
# question16()


# question 17
def question17():
    total = 0
    while True:
        amount = input().split()
        if not amount:
            break
        elif amount[0] == 'D':
            total += int(amount[1])
        elif amount[0] == 'W':
            total -= int(amount[1])
    print(total)
# question17()
