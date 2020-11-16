new_list = []
new_new_list = []
stop_word = 'Q'
def summa(aaa):
    numbers2 = aaa.split()
    for i in numbers2:
        new_list.append(i)
    if stop_word in new_list:
        new_list.remove(stop_word)
    for s in new_list:
        new_new_list.append(int(s))
    print(sum(new_new_list))
    new_list.clear()
    if stop_word in numbers2:
        return True
    else:
        return False


while True:
    if summa(input("vvedite tsifri: ")):
        breake