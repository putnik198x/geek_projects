def biggest_numbers(numbers):
    blank_list = []
    max_list = []
    numbers1 = []
    numbers1 = numbers.split()
    for i in numbers1:
        i = int(i)
        blank_list.append(i)
    max_list.append(max(blank_list))
    x = max(blank_list)
    blank_list.remove(x)
    max_list.append(max(blank_list))
    return print(max_list)

initial_list = input('введите три числа: ')
biggest_numbers(initial_list) # initial_list позиционный аргумент для numbers, включающий список