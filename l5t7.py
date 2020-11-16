import json
firms = {}
average_firms = []
with open ('aaa_ru.txt', 'r', encoding='UTF-8') as file_ru:
    lines = file_ru.readlines()
    for line in lines:
        firm, type, rev, costs = line.split()
        profit = int(rev) - int(costs)
        firms[firm] = profit
        if profit > 0:
            average_firms.append(profit)

aver_prof = sum(average_firms)/len(average_firms)
aaa = [firms, {'прибыль по компаниям: ': average_firms} ]

with open('aaa_ru.json', 'w') as json_ru:
    json.dump(aaa, json_ru)

with open ('aaa_ru.json') as json_ru:
    print(json.load(json_ru))