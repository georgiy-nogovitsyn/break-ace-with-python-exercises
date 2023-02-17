# question 100
def question100():
    n = int(input('Input num of words: '))
    freq = {}
    for x in range(n):
        word = input('Input word: ')
        if word not in freq.keys():
            freq[word] = 1
        else:
            freq[word] += 1
    for x in freq.values():
        print(x, end=' ')
# question100()


# question 101
def question101():
    st = input('Input a string: ')
    freq = {}
    for ch in st:
        freq[ch] = freq.get(ch, 0) + 1

    freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    for x in freq:
        print(x[0], x[1])
# question101()


# question 102
def question102():
    st = input('Input a string: ')
    letters, digits = 0, 0
    for ch in st:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
    print(f'Letters: {letters}\nDigits: {digits}')
# question102()


# question 103
def rec_sum(n, s):
    if n == 0:
        return s
    s += n
    return rec_sum(n-1, s)

num = int(input('Input: '))
print(rec_sum(num, 0))

