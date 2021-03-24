import math
class cell:
    def __init__(self, c):
        self.coat = c

    def __add__(self, other):
        return cell(self.coat + other.coat)

    def __sub__(self, other):
        if self.coat - other.coat > 0:
            return cell(self.coat - other.coat)
        else:
            return f'Соответствующее сообщение'
    def __mul__(self, other):
        return cell(self.coat * other.coat)
    def __floordiv__(self, other):
        return cell(math.ceil(self.coat / other.coat))
    def __str__(self):
        return f'Количество клеток: {self.coat}'

    @property
    def make_order(self):
        for i in range(self.coat // 5):
            print(f'*****')
        if self.coat % 5 > 0:
            print ('*' * (self.coat % 5))
            return ''
        else:
            return ''


cell_one = cell(103)
cell_two = cell(27)

print(cell_two.make_order)