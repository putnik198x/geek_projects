xxx = []
dictionary= []
d = 0
kol = int(input('количество товаров: ')).  # тут я опредлею количество лупов в цикле. Можно было сделать через стоп слово, но так мне показалось логичней
while d < kol:
    d = d + 1
    dic = []
    dic.append(d)
    x = {}
    c = input('ввыедите название товаров: ')
    x['название'] = c
    b = int(input('введите цену: ')) # я решил ограничится двумя позициями в словаре. 
    x['цена'] = b
    dic.append(x)
    kar = tuple(dic)
    xxx.append(kar)
    dictionary.append(x)
print(xxx)

x = input("показать аналитику (y или n): ") # по желанию пользователя вывожу аналитику. всего два варианта ответа - да или нет. 
if x == 'y':
    d = -1
    new_slovary = {}
    new_nazvanie = []
    new_tsena = []
    while d < kol-1:
        d = d + 1
        ccc = dictionary[d]
        new_nazvanie.append(ccc['название'])
        new_tsena.append(ccc['цена'])
        new_slovary['название'] = new_nazvanie
        new_slovary['цена'] = new_tsena
    print(new_slovary)
if x == 'n':
    print("спасибо за внимание")