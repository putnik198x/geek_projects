class Worker():
    name = ()
    surname = ()
    position = ()
    _income = {"wage": (), "bonus": ()}

class Position(Worker):
    def get_full_name(self):
        Worker.name = input("Enter the name: ")
        Worker.surname = input("Enter the Surname: ")
        Worker.position = input("Enter the position: ")

    def get_total_income(self):
        Worker._income["wage"] = int(input("Enter the wage: "))
        Worker._income["bonus"] = int(input("Enter the bonus: "))

qs = input('would you be interested to enter info about workers y/n: ')
if qs == 'y':
    Position.get_full_name(Worker)
    print(Worker.name)
    print('Name, Surname and Position are: ', Worker.name, Worker.surname, Worker.position)
else:
    Position.get_total_income(Worker)
    print('workers wage is: ', Worker._income["wage"])