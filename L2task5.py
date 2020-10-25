aaa = [7, 5, 3, 3, 2]
while True:
    k = int(input("vvedite naturalinoe chislo: "))
    aaa.append(k)
    aaa.sort(reverse=True)
    print(aaa)