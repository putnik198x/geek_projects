with open ('aaa_ru.txt', 'r', encoding='UTF-8') as file_ru:
    dic = {}
    lines = file_ru.readlines()
    for line in lines:
        a = line.split()
        key_value = a[0]
        el = []
        e = []
        for x in a[1:]:
            if '(' in x:
                i = sum([int(x[:x.find('(')])])
                el.append(i)
        elem_value = sum(el)
        dic[key_value[:-1]] = elem_value
    print(dic)