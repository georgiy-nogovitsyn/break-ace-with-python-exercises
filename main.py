#ex 1
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=', ')
print('\b')

#ex 2
num = int(input('here: '))
output = 1

for x in range(1, num+1):
    output = output * x

print(output)

#ex 3
integral = int(input('here: '))
output_dict = dict()
for i in (range(1, integral + 1)):
    output_dict[i] = i * i

print(output_dict)