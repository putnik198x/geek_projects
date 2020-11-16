x = int(input("Enter the income: "))
y = int(input("Enter the loses: "))
vir = x - y
if x > y:
    print ('financial results are good: ', x - y, 'profitability: ', x/y)
elif y < x:
    print('financial results are not good: ', y - x)
else:
    print('zero income: ', x - y)