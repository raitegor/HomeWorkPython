class Transport:
    # атрибуты класса
    a_count = 0

    # Конструктор
    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self.model = m
        self.year = y
        Auto.a_count += 1

    # методы класса
    def on_star(self, speed):
        print(f'go-go car {self.name}, with spped {speed}')

    def on_stop(self):
        print('stop!')

class Auto(Transport):
    def drift(self, n, m, y, p):
        super().__init__(n, m, y)
        self.pass_ = p
        print('Vg')



auto_1 =Auto('mazda', 'cx-9', 2021)
auto_1.on_star(35)
auto_1.drift()


# auto_1 = Auto('mazda', 'cx-9', 2021)
# print(auto_1.name)
# auto_1.on_star()
# print(auto_1.a_count)
# print()
#
# auto_2 = Auto('Lada', 'Niva', 2019)
# print(auto_2.name)
# print(auto_2.a_count)