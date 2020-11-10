class Stationery:
    def init(self, title):
        self.title = title

    def draw(self):
        info = 'Запуск отрисовки'
        return info

class Pen(Stationery):
    def init(self, title):
        self.title = title

    def draw(self):
        return f"запуск отрисовки ручкой: {self.title}"

class Pencil(Stationery):
    def init(self, title):
        self.title = title

    def draw(self):
        return f"запуск отрисовки корандашем: {self.title}"

class Handle(Stationery):
    def init(self, title):
        self.title = title

    def draw(self):
        return f"запуск отрисовки маркером: {self.title}"

r = Pen('ручка')
print(r.draw())

d = Handle('marker')
print(d.draw())