y = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
x = [y[i] for i in range(1, len(y)) if y[i] > y[i-1]]
print(x)