from itertools import count
x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
y = []

for i in x:
    aaa = x.count(i)
    if aaa < 2:
        y.append(i)
print(y)