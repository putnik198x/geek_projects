aaa = []

def parameters(x, y, c, v, b, n):
    aaa = []
    aaa.append(user_name)
    aaa.append(user_surname)
    aaa.append(user_year)
    aaa.append(user_city)
    aaa.append(user_email)

    return print(*aaa, sep=", ")


user_name = input("Введите имя: ")
user_surname = input("Введите фамилия: ")
user_year = input("Введите год: ")
user_city = input("Введите город: ")
user_tel = input("Введите телефон: ")
user_email =input("Введите почту: ")

parameters(user_name, user_surname, user_year, user_city, user_tel, user_email)