class Road:
    _length = ()
    _width = ()

    def calc(self):
        _length = int(input('ввудите длинну дороги: '))
        _width = int(input('ввудите ширину дороги: '))
        mass = int(input('ввудите массу асфальта: '))
        sant = int(input('ввудите толшину асфальта: '))
        massa = _length*_width*mass*sant
        print(massa,'тонн')

zapusk = Road()
print(zapusk.calc())