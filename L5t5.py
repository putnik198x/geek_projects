with open ('aaa_ru.txt', 'r', encoding='UTF-8') as file_ru:
    line = file_ru.readline()
    a =  line.split()
    numbers = []
    for num in a:
        numbers.append(int(num))
    print(sum(numbers))