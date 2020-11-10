with open ('aaa_ru.txt', 'r', encoding='UTF-8') as file_ru:
    sotrudniki = []
    zarplati = []
    lines = file_ru.readlines()
    for line in lines:
        words = line.split()
        print(line)
        zarplati.append(int(words[1]))
        if int(words[1]) < 20000:
            sotrudniki.append(words[0])
    print('Сумма зарплат: ', sum(zarplati))
    print('Следующие сотрудники имеют меньше: ', sotrudniki)