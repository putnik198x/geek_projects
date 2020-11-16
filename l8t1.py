import random

class Game:
    loto_1player = [[], [], []]
    loto_2player = [[], [], []]

    def loto_game_for_loto_1player(self):
        k = 0
        for i in range(0,9):
            n = random.randint(0,90)
            self.loto_1player[0].append(n)
        while k < 9:
            n = random.randint(0, 90)
            if n not in self.loto_1player[0] and n not in self.loto_1player[1]:
                self.loto_1player[1].append(n)
                k = k + 1
        k=0
        while k < 9:
            n = random.randint(0, 90)
            if n not in self.loto_1player[0] and n not in self.loto_1player[1] and n not in self.loto_1player[2]:
                self.loto_1player[2].append(n)
                k = k + 1

        for i in sorted(self.loto_1player):
            x = []
            while len(x) < 4:
                index = random.randint(0, 8)
                if index not in x:
                    x.append(index)
                    i[index] = '_'
        print('Пример карточки Первого игрока')
        print(*self.loto_1player[0])
        print(*self.loto_1player[1])
        print(*self.loto_1player[2])
        print('___________________')

    def loto_game_for_loto_2player(self):
        k = 0
        for i in range(0, 9):
            n = random.randint(0, 90)
            self.loto_2player[0].append(n)
        while k < 9:
            n = random.randint(0, 90)
            if n not in self.loto_2player[0] and n not in self.loto_2player[1]:
                self.loto_2player[1].append(n)
                k = k + 1
        k = 0
        while k < 9:
            n = random.randint(0, 90)
            if n not in self.loto_2player[0] and n not in self.loto_2player[1] and n not in self.loto_2player[2]:
                self.loto_2player[2].append(n)
                k = k + 1

        for i in sorted(self.loto_2player):
            x = []
            while len(x) < 4:
                index = random.randint(0, 8)
                if index not in x:
                    x.append(index)
                    i[index] = '_'
        print('Пример карточки Второго игрока')
        print(*self.loto_2player[0])
        print(*self.loto_2player[1])
        print(*self.loto_2player[2])
        print('___________________')

class Player(Game):

    def hod_pervogo_igroka(self):
        self.number = random.randint(0, 90)

        print('Ход первого игрока: ')
        print(*self.loto_1player[0])
        print(*self.loto_1player[1])
        print(*self.loto_1player[2])

        print('боченок лоtо: ', self.number)
        otvet = input('есть ли число в списке? n/y: ')

        if otvet == 'y':
            if self.number in self.loto_1player[0] or self.number in \
                    self.loto_1player[1] or self.number in self.loto_1player[2]:
                if self.number in self.loto_1player[0]:
                    index = self.loto_1player[0].index(self.number)
                    self.loto_1player[0][index] = '_'
                if self.number in self.loto_1player[1]:
                    index = self.loto_1player[1].index(self.number)
                    self.loto_1player[1][index] = '_'
                if self.number in self.loto_1player[2]:
                    index = self.loto_1player[2].index(self.number)
                    self.loto_1player[2][index] = '_'

            else:
                print('Вы проиграли!')

        elif otvet == 'n':
            if self.number in self.loto_1player[0] or self.number in \
                    self.loto_1player[1] or self.number in self.loto_1player[2]:
                print('Вы проиграли!')


            else:
                print('продолжаем!')

        print('Ход второго игрока: ')
        print(*self.loto_2player[0])
        print(*self.loto_2player[1])
        print(*self.loto_2player[2])

        print('боченок лоtо: ', self.number)
        if self.number in self.loto_2player[0] or self.number in \
                self.loto_2player[1] or self.number in self.loto_2player[2]:
            if self.number in self.loto_2player[0]:
                index = self.loto_2player[0].index(self.number)
                self.loto_2player[0][index] = '_'
            if self.number in self.loto_1player[1]:
                index = self.loto_2player[1].index(self.number)
                self.loto_2player[1][index] = '_'
            if self.number in self.loto_2player[2]:
                index = self.loto_2player[2].index(self.number)
                self.loto_2player[2][index] = '_'

        else:
            print('Нет числа в карточке')



class loto_game(Player):
    def igra(self):
        while True:
            Player.hod_pervogo_igroka(self)

fff = Game()
Game.loto_game_for_loto_1player(fff)
Game.loto_game_for_loto_2player(fff)
loto_game.igra(fff)







