from itertools import count, cycle

x= []

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
x_length = len(x)
c = 0
for i in cycle(x):
    if c == x_length:
        break
    print(i)
    c += 1