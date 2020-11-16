x = int(input("Enter the  natural number: "))
c = 0
c1 = 0
while x > 0:
    c = x % 10
    if c > c1:
        c1 = c
    x = x // 10
print('The biggest number is', c1)