xxx = int(input("Enter seconds: "))
min1 = xxx // 60
sec = xxx-min1*60
hrs = min1 //60
min2 = min1-hrs*60
print('%s:%s:%s' % (hrs, min2, sec))