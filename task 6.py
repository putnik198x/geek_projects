number = int(input("сколько километров: "))
finish = int(input("результат спортсмена составляет не менее: "))
day = 1
print(day, '-й день: ', number)
while True:
    number += number * 0.10
    if number <= finish:
        day = day+1
        print(day, '-й день: ', number)
    elif True:
        number += number * 0.10
        day = day+1
        print(day, '-й день: ', number)
        break

print('Ответ: на ', day, '-й день спортсмен достиг результата — не менее', finish, 'км.')