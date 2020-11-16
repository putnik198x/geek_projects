def int_func(text):
    separate_list = my_list.split()
    new_dic = []
    for word in separate_list:
        new_dic.append(word.title())
        words = list(new_dic)
    return words


my_list = input("Введите слова: ")
print(*int_func(my_list), sep=", ")