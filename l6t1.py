import time

class trafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(self.__color[0])
            time.sleep(2)
            print(self.__color[1])
            time.sleep(1)
            print(self.__color[2])
            time.sleep(2)

zapusk = trafficLight()
print(zapusk.running())