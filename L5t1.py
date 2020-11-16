with open ('test1.txt', 'w+', encoding='UTF-8') as file_ru:
    while True:
        text = input('введите текст: ')
        stroca = [text, '\n']
        file_ru.writelines(stroca)
        if text == '':
            break