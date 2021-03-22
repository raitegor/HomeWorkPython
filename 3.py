class Worker:

    def __init__(self, n, sn, pos, w, b):
        self.name = n
        self.surname = sn
        self.position = pos
        self.wage = w
        self.bonus = b
        self.income = {'wage': self.wage, 'bonus': self.bonus}




class Position(Worker):
    def get_ful_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income (self):
        total_income = self.income['wage'] + self.income['bonus']
        print(f'Доход сотрудника {total_income}')

persone = Position ('Саруман', 'Мудрый', 'Маг', 1000, 700)
persone.get_ful_name()
persone.get_total_income()


