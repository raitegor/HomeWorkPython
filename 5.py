class Stationery:
    def __init__(self, t):
        self.title = t
    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil (Stationery):
    def draw (self):
        print(f'Отрисовка нарисована')

class Handle (Stationery):
    def draw(self):
        print(f'Маркер можно стереть')

a = Stationery('Pen')
a.draw()

b = Pen('Pen')
b.draw()

c = Pencil('Pencil')
c.draw()

d = Handle('Handle')
d.draw()
