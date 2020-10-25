aaa = input('vvedite text: ')
bbb = aaa.split()
x = 0
for el in bbb:
    while True:
        x = x+1
        print(x, el[:5]) #Если в слово длинное, выводить только первые 5 букв в слове.
        break