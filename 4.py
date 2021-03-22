import random
class Car:
    def __init__(self, s, c, n, pol):
        self.max_speed = s
        self.color = c
        self.name = n
        self.is_police = pol

    def go (self):
        print(f'Машина {self.name}, {self.color} - едет с максимальной скоростью {self.max_speed} км/ч')

    def stop(self):
        print(f'Машина {self.name}, {self.color} - остановилась')

    def turn (self, where):
        print(f'Машина {self.name}, {self.color} - поворачивает {where}')
    def show_speed(self):
        print(f' Скорость: {random.randint(0, self.max_speed)} км/ч ')


class TownCar (Car):
    def __init__(self, s, c, n, pol, seat):
        super().__init__(s, c, n, pol)
        self.seat = seat
    def show_speed(self):
        speed = random.randint(0, self.max_speed)
        if speed > 60 :
            print(f'Скорость {speed} км/ч, вы привышаете!')
        else:
            print(f'Скорость {speed} км/ч, не превышает разрешенной')

class WorkCar (Car):
    def show_speed(self):
        speed = random.randint(0, self.max_speed)
        if speed > 40:
            print(f'Скорость {speed} км/ч, вы привышаете!')
        else:
            print(f'Скорость {speed} км/ч, не превышает разрешенной')

auto_1 = Car (100, 'Красный', 'Toyota', False)
auto_1.show_speed()
auto_1.go()

print()
auto_2 = WorkCar(120, 'Серый', 'Lada Largus', False)
auto_2.show_speed()