import math

def fact(a):
    for i in range(1, a+1):
        yield i

g = fact(int(input("vv: " )))


for i in g:
    print(math.factorial(i))