class Car:
    speed = int()
    color= ('The cars color is red')
    name = ('Toyota')
    is_police = True
    TownCar = ('Avensis')
    WorkCar = ('Prado')
    def go(self):
        print(Car.name, "is on its way")
    def stop(self):
        print(Car.name, 'has stopped')
    def turn(direction):
        if direction == 'left':
            left = 'car turned left'
            return(left)
        elif direction == 'right':
            print('car turned right')
        else:
            print('car didnt turn anywhere')
    def show_speed(self):
        Car.speed = self
        print('The speed is ', Car.speed)
        tipe_of_car = input('Is your car Avensis ot Prado? ')
        if tipe_of_car == Car.TownCar:
            if Car.speed >= 60:
                print('Speadlimit violation!')
            else:
                print("tot ok")
        if tipe_of_car == Car.WorkCar:
            if Car.speed >= 40:
                print('Speadlimit violation!')
            else:
                print("tot ok")



print(Car.color)
print(Car.go(Car.name))
print(Car.turn('left'))
aaa = int(input('what is the current speed?'))
print(Car.show_speed(aaa))