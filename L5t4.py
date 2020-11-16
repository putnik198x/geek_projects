with open ('aaa_ru.txt', 'w+', encoding='UTF-8') as file_ru:
    with open('aaa.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            x = line.strip()
            print(x)
            y = x.split(' — ')
            print(y)
            if y[1] == '1':
                b = line.replace("One", "Oдин")
                file_ru.write(b)
            if y[1] == '2':
                b1 = line.replace('Two', 'два')
                file_ru.write(b1)
            if y[1] == '3':
                b = line.replace('Three', 'три')
                file_ru.write(b)
            if y[1] == '4':
                b = line.replace('Four', 'четыре')
                file_ru.write(b)