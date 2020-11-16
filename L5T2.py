with open('test1.txt', 'r') as file:
    lines = file.readlines()
    stroka = 0
    for line in lines:
        stroka = stroka+1
        words = len(line.split())
        print('количество слов: ', words)

print('общее кол-во строк: ', stroka)