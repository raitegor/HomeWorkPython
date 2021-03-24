from abc import ABC, abstractmethod

class Clothes:
    result = 0
    def __init__(self, p_1):
        self.p_1 = p_1
    @property
    @abstractmethod
    def consum(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consum + other.consum
        return Clothes(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f'{res}'


class Jacket (Clothes):
    @property
    def consum (self):
        return round((self.p_1/6.5) + 0.5)


class Smoking (Clothes):
    @property
    def consum(self):
        return round((2 * self.p_1) + 0.3)


jacket = Jacket(34)
smoking = Smoking(34)

print (jacket + smoking)
