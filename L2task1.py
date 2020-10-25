x = []
m = 0
while m <= 1 :
    m = m + 1
    c = int(input("vvedite tsifru: "))
    x.append(c)
    c = input("vvedite text: ")
    x.append(c)
print(x)
for i in x:
    print(type(i))
